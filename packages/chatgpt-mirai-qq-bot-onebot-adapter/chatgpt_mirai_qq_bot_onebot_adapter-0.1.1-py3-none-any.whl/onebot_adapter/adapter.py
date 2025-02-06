import asyncio
import functools
import time
import random

from aiocqhttp import CQHttp, Event
from aiocqhttp import MessageSegment
from framework.im.adapter import IMAdapter
from framework.im.message import IMMessage, TextMessage, AtElement
from framework.im.sender import ChatSender, ChatType
from framework.logger import get_logger
from framework.workflow.core.dispatch.dispatcher import WorkflowDispatcher

from .config import OneBotConfig
from .handlers.message_result import MessageResult
from .utils.message import create_message_element

logger = get_logger("OneBot")


class OneBotAdapter(IMAdapter):
    def __init__(self, config: OneBotConfig, dispatcher: WorkflowDispatcher):
        super().__init__()
        self.config = config  # 配置
        self.dispatcher = dispatcher  # 工作流调度器
        self.bot = CQHttp()  # 初始化CQHttp

        self._server_task = None  # 反向ws任务
        self.heartbeat_states = {}  # 存储每个 bot 的心跳状态
        self.heartbeat_interval = self.config.heartbeat_interval  # 心跳间隔
        self.heartbeat_timeout = self.config.heartbeat_interval * 2  # 心跳超时
        self._heartbeat_task = None  # 心跳检查任务

        # 注册事件处理器
        self.bot.on_meta_event(self._handle_meta)  # 元事件处理器
        self.bot.on_notice(self.handle_notice)  # 通知处理器
        self.bot.on_message(self._handle_msg)  # 消息处理器

    async def _check_heartbeats(self):
        """
        检查所有连接的心跳状态

        兼容一些不发送disconnect事件的bot平台
        """
        while True:
            current_time = time.time()
            for self_id, last_time in list(self.heartbeat_states.items()):
                if current_time - last_time > self.heartbeat_timeout:
                    logger.warning(f"Bot {self_id} disconnected (heartbeat timeout)")
                    self.heartbeat_states.pop(self_id, None)
            await asyncio.sleep(self.heartbeat_interval)

    async def _handle_meta(self, event: Event):
        """处理元事件"""
        self_id = event.self_id

        if event.get('meta_event_type') == 'lifecycle':
            if event.get('sub_type') == 'connect':
                logger.info(f"Bot {self_id} connected")
                self.heartbeat_states[self_id] = time.time()

            elif event.get('sub_type') == 'disconnect':
                # 当bot断开连接时,  停止该bot的事件处理
                logger.info(f"Bot {self_id} disconnected")
                self.heartbeat_states.pop(self_id, None)

        elif event.get('meta_event_type') == 'heartbeat':
            self.heartbeat_states[self_id] = time.time()

    async def _handle_msg(self, event: Event):
        """处理消息的回调函数"""
        message = self.convert_to_message(event)

        await self.dispatcher.dispatch(self, message)

    async def handle_notice(self, event: Event):
        """处理通知事件"""
        pass

    def convert_to_message(self, event: Event) -> IMMessage:
        """将 OneBot 消息转换为统一消息格式"""
        # 构造发送者信息
        sender_info = event.sender or {}
        if event.group_id:
            sender = ChatSender.from_group_chat(
                user_id=str(event.user_id),
                group_id=str(event.group_id),
                display_name=sender_info.get('nickname', str(event.user_id))
            )
        else:
            sender = ChatSender.from_c2c_chat(
                user_id=str(event.user_id),
                display_name=sender_info.get('nickname', str(event.user_id))
            )

        # 转换消息元素
        message_elements = []
        for msg in event.message:
            try:
                element = create_message_element(msg['type'], msg['data'])
                if element:
                    message_elements.append(element)
            except Exception as e:
                logger.error(f"Failed to convert message element: {e}")

        return IMMessage(
            sender=sender,
            message_elements=message_elements,
            raw_message=event
        )

    def convert_to_message_segment(self, message: IMMessage) -> list[MessageSegment]:
        """将统一消息格式转换为 OneBot 消息段列表"""
        segments = []

        # 消息类型到转换方法的映射
        segment_converters = {
            'text': lambda data: MessageSegment.text(data['text']),
            'image': lambda data: MessageSegment.image(data['url']),
            'at': lambda data: MessageSegment.at(data['data']['qq']),
            'reply': lambda data: MessageSegment.reply(data['data']['id']),
            'face': lambda data: MessageSegment.face(int(data['data']['id'])),
            'record': lambda data: MessageSegment.record(data['data']['url']),
            'voice': lambda data: MessageSegment.record(data['url']),
            'video': lambda data: MessageSegment.video(data['data']['file']),
            'json': lambda data: MessageSegment.json(data['data']['data'])
        }

        for element in message.message_elements:
            try:
                data = element.to_dict()
                msg_type = data['type']
                
                if msg_type in segment_converters:
                    segment = segment_converters[msg_type](data)
                    segments.append(segment)
            except Exception as e:
                logger.error(f"Failed to convert message segment type {msg_type}: {e}")

        return segments

    async def start(self):
        """启动适配器"""
        try:
            logger.info(f"Starting OneBot adapter on {self.config.host}:{self.config.port}")

            # 使用现有的事件循环
            self._heartbeat_task = asyncio.create_task(self._check_heartbeats())
            self._server_task = asyncio.create_task(self.bot.run_task(
                host=self.config.host,
                port=int(self.config.port)
            ))

            logger.info(f"OneBot adapter started")
        except Exception as e:
            logger.error(f"Failed to start OneBot adapter: {str(e)}")
            raise

    async def stop(self):
        """停止适配器"""
        try:
            # 1. 停止消息处理
            if hasattr(self.bot, '_bus'):
                self.bot._bus._subscribers.clear()  # 清除所有事件监听器
                # 等待所有正在处理的消息完成
                await asyncio.sleep(0.5)

            # 2. 停止心跳检查
            if self._heartbeat_task and not self._heartbeat_task.done():
                self._heartbeat_task.cancel()
                try:
                    await asyncio.wait_for(self._heartbeat_task, timeout=1.0)
                except (asyncio.CancelledError, asyncio.TimeoutError):
                    pass
                self._heartbeat_task = None

            # 3. 关闭 WebSocket 连接
            if hasattr(self.bot, '_websocket') and self.bot._websocket:
                if not isinstance(self.bot._websocket, functools.partial):  # 检查类型
                    await self.bot._websocket.close()

            # 4. 关闭 Hypercorn 服务器
            if hasattr(self.bot, '_server_app'):
                try:
                    # 获取 Hypercorn 服务器实例
                    server = getattr(self.bot._server_app, '_server', None)
                    if server:
                        # 停止接受新连接
                        server.close()
                        await server.wait_closed()

                    # 关闭所有 WebSocket 连接
                    for client in getattr(self.bot._server_app, 'websocket_clients', []):
                        if hasattr(client, 'close'):
                            await client.close()

                    # 关闭 ASGI 应用
                    if hasattr(self.bot._server_app, 'shutdown'):
                        await self.bot._server_app.shutdown()

                except Exception as e:
                    logger.warning(f"Error shutting down Hypercorn server: {e}")

            # 5. 取消所有相关任务
            tasks = [t for t in asyncio.all_tasks()
                     if any(name in str(t) for name in ['hypercorn', 'quart', 'websocket'])
                     and not t.done()]

            if tasks:
                # 取消任务
                for task in tasks:
                    task.cancel()

                # 等待任务取消完成
                try:
                    await asyncio.wait(tasks, timeout=2.0)
                except (asyncio.CancelledError, asyncio.TimeoutError):
                    pass

            # 6. 清理状态
            self.heartbeat_states.clear()

            logger.info("OneBot adapter stopped")
        except Exception as e:
            logger.error(f"Error stopping OneBot adapter: {e}")

    async def recall_message(self, message_id: int, delay: int = 0):
        """撤回消息

        Args:
            message_id: 要撤回的消息ID
            delay: 延迟撤回的时间(秒) 默认为0表示立即撤回
        """
        if delay > 0:
            await asyncio.sleep(delay)
        await self.bot.delete_msg(message_id=message_id)

    async def send_message(self, message: IMMessage, recipient: ChatSender) -> MessageResult:
        """发送消息"""
        result = MessageResult()
        try:
            segments = self.convert_to_message_segment(message)

            for i, segment in enumerate(segments):
                # 如果不是第一条消息,添加随机延时
                if i > 0:
                    # 获取消息内容长度(如果是文本)
                    content_length = len(str(segment)) if isinstance(segment, MessageSegment) else 10
                    # 根据内容长度和随机因子计算延时
                    duration = content_length * 0.1 + random.uniform(0.5, 1.5)
                    await asyncio.sleep(duration)

                if recipient.chat_type == ChatType.GROUP:
                    send_result = await self.bot.send_group_msg(
                        group_id=int(recipient.group_id),
                        message=segment
                    )
                else:
                    send_result = await self.bot.send_private_msg(
                        user_id=int(recipient.user_id),
                        message=segment
                    )

                result.message_id = send_result.get('message_id')
                result.raw_results.append({"action": "send", "result": send_result})

            return result

        except Exception as e:
            result.success = False
            result.error = f"Error in send_message: {str(e)}"
            return result

    async def send_at_message(self, group_id: str, user_id: str, message: str):
        """发送@消息"""
        bot_sender = ChatSender.from_group_chat(
            user_id="<@bot>",
            group_id=group_id,
            display_name="Bot"
        )
        
        msg = IMMessage(
            sender=bot_sender,
            message_elements=[
                AtElement(user_id),
                TextMessage(" " + message)
            ]
        )
        
        recipient = ChatSender.from_group_chat(
            user_id="<@bot>",
            group_id=group_id,
            display_name="Bot"
        )
        
        await self.send_message(msg, recipient)

    async def mute_user(self, group_id: str, user_id: str, duration: int):
        """禁言用户"""
        await self.bot.set_group_ban(
            group_id=int(group_id),
            user_id=int(user_id),
            duration=duration
        )

    async def unmute_user(self, group_id: str, user_id: str):
        """解除禁言"""
        await self.mute_user(group_id, user_id, 0)

    async def kick_user(self, group_id: str, user_id: str):
        """踢出用户"""
        await self.bot.set_group_kick(
            group_id=int(group_id),
            user_id=int(user_id)
        )
