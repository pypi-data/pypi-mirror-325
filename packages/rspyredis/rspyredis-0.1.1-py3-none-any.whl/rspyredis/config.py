from typing import Any


class RedisConfig:
    def __init__(self):
        self._config_data = {}

    def set_redis_host(self, host: str):
        self._config_data["redis_host"] = host

    def set_redis_port(self, port: int):
        self._config_data["redis_port"] = port

    def set_redis_db(self, database: str):
        self._config_data["redis_db"] = database

    def set_redis_password(self, password: str):
        self._config_data["redis_password"] = password

    def set_redis_username(self, username: str):
        self._config_data["redis_username"] = username

    def set_redis_ssl(self, ssl: bool):
        self._config_data["redis_ssl"] = ssl

    def get(self, key: str, default: Any = None):
        return self._config_data.get(key, default)
