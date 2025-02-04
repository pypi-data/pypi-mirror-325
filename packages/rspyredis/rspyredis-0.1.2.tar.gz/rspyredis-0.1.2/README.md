# Redis

A light Python package for Redis management.

## Features
- **Singleton Redis Connection**: Ensures a single instance of the Redis connection for both synchronous and asynchronous operations.
- **Flexible Configuration**: Easily configure the Redis connection with options for host, port, database, username, password, and SSL support.
- **Synchronous Redis Client**: Provides a synchronous Redis client for basic Redis operations such as setting and getting keys.
- **Asynchronous Redis Client**: Supports asynchronous Redis operations using `asyncio`, enabling non-blocking interactions with Redis.
- **Automatic URL Construction**: Automatically constructs the Redis connection URL based on the provided configuration, including optional username, password, and SSL support.
- **Error Handling**: Raises clear errors if required configuration values are missing, helping to debug connection issues quickly.
- **Easy Integration**: Designed to integrate easily into any Python project for managing Redis connections without additional overhead.


## Installation

You can install the package directly with pip.

```bash
pip install rspyredis
```
