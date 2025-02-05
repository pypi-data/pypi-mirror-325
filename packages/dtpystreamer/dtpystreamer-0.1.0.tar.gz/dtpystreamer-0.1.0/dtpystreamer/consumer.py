import json
import time
from dtpyredis.connection import RedisInstance
from .utils import retry_on_failure


class Consumer:

    def __init__(self, redis_instance: RedisInstance, consumer_name: str):
        self.consumer_name: str = consumer_name
        self._handlers: dict[str, list] = {}
        self._channels = []
        self._redis_instance = redis_instance
        self._redis_client = self._redis_instance.get_redis_client()

    def _consumer_group_exists(self, channel_name: str, consumer_group: str) -> bool:
        try:
            groups = self._redis_client.xinfo_groups(channel_name)
            return any(group['name'].decode('utf-8') == consumer_group for group in groups)
        except Exception as e:
            return False

    def register_channel(self, channel_name: str, consumer_group: str):
        if not self._consumer_group_exists(channel_name, consumer_group):
            try:
                self._redis_client.xgroup_create(channel_name, consumer_group, '$', mkstream=True)
            except Exception as e:
                print(f"Error creating consumer group {consumer_group} for channel {channel_name}: {e}")
        self._channels.append((channel_name, consumer_group))
        self._handlers[channel_name] = []

    def register_handler(self, channel_name: str, handler_func):
        self._handlers[channel_name].append(handler_func)

    @retry_on_failure
    def consume_messages(self, channel: str, consumer_group: str, block_time: float):
        messages = self._redis_client.xreadgroup(consumer_group, self.consumer_name, {channel: ">"}, block=block_time * 1000, count=1)
        for message in messages:
            stream_name, message_data = message
            message_id, message_content = message_data[0]
            name = message_content.get(b'name')
            body = message_content.get(b'body')
            if name and body:
                name = name.decode()
                body = json.loads(body.decode())
                for handler in self._handlers.get(channel, []):
                    handler(name=name, **body)
                self._redis_client.xack(channel, consumer_group, message_id)

    def persist_consume_messages(self, channel: str, consumer_group: str, rest_time: float, block_time: float):
        while True:
            self.consume_messages(channel=channel, consumer_group=consumer_group, block_time=block_time)
            if rest_time > 0:
                time.sleep(rest_time)

    def consume_all_channels(self, block_time: float):
        for channel, consumer_group in self._channels:
            self.consume_messages(channel=channel, consumer_group=consumer_group, block_time=block_time)

    def persist_consume_all_channels(self, rest_time: float, block_time: float):
        while True:
            self.consume_all_channels(block_time=block_time)
            if rest_time > 0:
                time.sleep(rest_time)
