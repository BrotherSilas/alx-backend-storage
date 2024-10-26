#!/usr/bin/env python3
"""
Module for finding documents by topic in MongoDB
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic: topic searched

    Returns:
        list of schools having the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
