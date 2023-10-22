#!/usr/bin/env python3


import uuid
import redis
from typing import Union, Callable
from functools import wraps


class Cache:
    """
    This class represents a caching mechanism using Redis.

    It allows you to store data in
    Redis using randomly generated key
    """

    def __init__(self):
        """
        Initialize the Cache class and connect to Redis.

        This method creates an instance of the
        Redis client and flush
        instance using the flushdb method.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis
        using a randomly generated key.

        :param data: The data to be stored
        :return: The randomly generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


def count_calls(method: Callable):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = methods.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


if __name__ == "__main__":
    main()
