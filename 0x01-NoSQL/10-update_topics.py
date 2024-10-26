#!/usr/bin/env python3
"""
Module for updating documents in MongoDB
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name: school name to update
        topics: list of topics approached in the school

    Returns:
        Nothing
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
