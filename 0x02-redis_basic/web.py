#!/usr/bin/env python3
"""
Module for implementing a web cache and tracker.
"""
import redis
import requests
from functools import wraps
from typing import Callable
from datetime import timedelta


def track_url_access(fn: Callable) -> Callable:
    """Decorator to track how many times a URL is accessed"""
    @wraps(fn)
    def wrapper(url: str) -> str:
        # Create Redis client
        redis_client = redis.Redis()

        # Create counter key for this URL
        count_key = f"count:{url}"

        # Increment the access counter
        redis_client.incr(count_key)

        # Get the page content (either from cache or by calling the function)
        result = fn(url)

        return result
    return wrapper


def cache_page(expiration: int = 10) -> Callable:
    """Decorator to cache webpage content"""
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(url: str) -> str:
            # Create Redis client
            redis_client = redis.Redis()

            # Create cache key for this URL
            cache_key = f"cache:{url}"

            # Try to get cached content
            cached_page = redis_client.get(cache_key)
            if cached_page:
                return cached_page.decode('utf-8')

            # If not in cache, get fresh content
            page_content = fn(url)

            # Cache the new content with expiration
            redis_client.setex(cache_key,
                               timedelta(seconds=expiration),
                               page_content)

            return page_content
        return wrapper
    return decorator


@track_url_access
@cache_page()
def get_page(url: str) -> str:
    """
    Get the HTML content of a URL and cache it for 10 seconds.
    Also tracks the number of times the URL is accessed.

    Args:
        url (str): The URL to fetch

    Returns:
        str: The HTML content of the page
    """
    response = requests.get(url)
    return response.text
