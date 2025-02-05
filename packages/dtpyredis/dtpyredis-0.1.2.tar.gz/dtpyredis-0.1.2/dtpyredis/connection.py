import urllib.parse
import redis
from contextlib import asynccontextmanager
from redis.asyncio import Redis as AsyncRedis
from typing import AsyncGenerator
from .config import RedisConfig


class RedisInstance:

    def __init__(self, redis_config: RedisConfig = None):
        self.redis_url = None
        self.config = redis_config
        self._set_redis_url()

    def _set_redis_url(self):
        required_settings = ['redis_host', 'redis_port', 'redis_db']
        for setting in required_settings:
            if not self.config.get(setting):
                raise ValueError(f"Missing required Redis setting: {setting}")

        redis_ssl = self.config.get('redis_ssl', False)
        redis_host = self.config.get('redis_host')
        redis_port = self.config.get('redis_port')
        redis_db = self.config.get('redis_db')
        redis_username = self.config.get('redis_username')
        redis_password = self.config.get('redis_password')

        username = urllib.parse.quote(redis_username) if redis_username else ''
        password = urllib.parse.quote(redis_password) if redis_password else ''

        if username and password:
            auth_part = f"{username}:{password}@"
        elif password:
            auth_part = f":{password}@"
        elif username:
            auth_part = f"{username}@"
        else:
            auth_part = ''

        if redis_ssl:
            protocol = 'rediss'
        else:
            protocol = 'redis'

        self.redis_url = f"{protocol}://{auth_part}{redis_host}:{redis_port}/{redis_db}"

    def get_redis_url(self) -> str:
        return self.redis_url

    def get_redis_client(self) -> redis.Redis:
        return redis.Redis.from_url(self.get_redis_url())

    def get_redis(self) -> redis.Redis:
        redis_client = self.get_redis_client()
        yield redis_client

    async def get_async_redis_client(self) -> AsyncRedis:
        return AsyncRedis.from_url(self.get_redis_url())

    @asynccontextmanager
    async def get_async_redis(self) -> AsyncGenerator[AsyncRedis, None]:
        async_redis_client = await self.get_async_redis_client()
        try:
            yield async_redis_client
        finally:
            await async_redis_client.close()
