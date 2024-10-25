#!/usr/bin/env python3
"""
Implements a simple web page caching system and access counter.
"""
import redis
import requests
from typing import str


def get_page(url: str) -> str:
    """
    Gets the HTML content of a particular URL and caches it for 10 seconds.
    Also tracks how many times a URL is accessed.

    Args:
        url: string URL to fetch

    Returns:
        str: the content of the URL
    """
    # Initialize Redis client
    redis_client = redis.Redis()
    
    # Define keys
    count_key = f"count:{url}"
    content_key = f"cached:{url}"
    
    # Increment the access counter
    redis_client.incr(count_key)
    
    # Try to get cached content
    content = redis_client.get(content_key)
    if content:
        return content.decode('utf-8')
    
    # If not in cache, fetch from web
    response = requests.get(url)
    html_content = response.text
    
    # Cache the content for 10 seconds
    redis_client.setex(content_key, 10, html_content)
    
    return html_content

