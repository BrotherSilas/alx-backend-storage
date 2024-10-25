#!/usr/bin/env python3
"""
This module createss a Cache class using Redis for storage.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    A cache system using Redis for storage.
    This class provides methods to store and retrieve data using Redis as a backend.
    """
    
    def __init__(self):
        """
        Initialize the Cache with a Redis connection and clear any existing data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key.
        
        Args:
            data: The data to store (can be str, bytes, int, or float)
            
        Returns:
            str: The key under which the data is stored
        """
        # Generate a random key using uuid
        key = str(uuid.uuid4())
        
        # Store the data in Redis
        self._redis.set(key, data)
        
        return key
    
