import urllib.parse
import redis
from contextlib import asynccontextmanager
from redis.asyncio import Redis as AsyncRedis
from typing import AsyncGenerator, Optional
from .config import Config
from .wrappers import singleton_class


@singleton_class
class RedisInstance:

    def __init__(self):
        self.redis_url = None
        self.config = Config()
        self._set_redis_url()

    def _set_redis_url(self):
        """
        Constructs the Redis connection URL based on the current settings,
        including username and password if provided.

        Returns:
            str: The Redis connection URL.

        Raises:
            ValueError: If any required Redis setting is missing.
        """
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


def get_redis_instance() -> Optional[RedisInstance]:
    try:
        return RedisInstance()
    except:
        return None
