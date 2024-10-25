#!/usr/bin/env python3
"""
This module implements a Cache class using Redis for storage with tracking
and history features.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called.

    Args:
        method: The method to be counted

    Returns:
        Callable: The wrapped method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Get the qualified name of the method as the key
        key = method.__qualname__
        # Increment the counter in Redis
        self._redis.incr(key)
        # Execute the original method
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function.

    Args:
        method: The method to store history for

    Returns:
        Callable: The wrapped method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Create input and output list keys using the method's qualified name
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store the input arguments as a string
        self._redis.rpush(input_key, str(args))

        # Execute the method and get the result
        result = method(self, *args, **kwargs)

        # Store the output
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.

    Args:
        method: The method to display history for
    """
    # Get the Redis instance from the cache class
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    # Get the number of calls
    calls = int(redis_instance.get(method_name) or 0)

    print(f"{method_name} was called {calls} times:")

    # Get inputs and outputs
    inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)

    # Print each call
    for input_args, output in zip(inputs, outputs):
        input_str = input_args.decode('utf-8')
        output_str = output.decode('utf-8')
        print(f"{method_name}(*{input_str}) -> {output_str}")


class Cache:
    """
    A cache system using Redis for storage with tracking and history features.
    """

    def __init__(self):
        """
        Initialize the Cache with a Redis connection and clear any existing data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key.

        Args:
            data: The data to store (can be str, bytes, int, or float)

        Returns:
            str: The key under which the data is stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Get data from Redis and convert it back to its original type.

        Args:
            key: The key to look up
            fn: Optional function to convert the data back to its original type

        Returns:
            The data in its original type
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Get a string value from Redis.

        Args:
            key: The key to look up

        Returns:
            str: The stored string
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Get an integer value from Redis.

        Args:
            key: The key to look up

        Returns:
            int: The stored integer
        """
        return self.get(key, lambda d: int(d))
