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

    @call_history
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

    @count_calls
    def get(self, key: str, fn: Callable = None) -> Union[
            str,
            bytes,
            int,
            float,
            None
       ]:
        """
        Retrieve data from Redis based on the provided key.

        :param key: The key to retrieve data
        :param fn: Optional callable to convert data back
        :return: Data retrieved from Redis, or None
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve string data from Redis based on key

        :param key: Key to retrieve string data
        :return: The string data
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve integer data

        :param key: The key to retrieve int data
        :return: the integer data from Redis
        """
        return self.get(key, fn=int)

    def replay(self, method: Callable):
        """
        Display the history of calls for a particular function.

        :param method: The function for which to display the history
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        for input_data, output_data in zip(inputs, outputs):
            print(f"Input: {input_data}, Output: {output_data}")


def count_calls(method: Callable):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)


def call_history(method: Callable):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


if __name__ == "__main__":
    pass
