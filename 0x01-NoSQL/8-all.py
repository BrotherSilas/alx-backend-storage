#!/usr/bin/env python3
"""Module for MongoDB operations with Python"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """Lists all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list of documents or empty list if none
    """
    return [doc for doc in mongo_collection.find()]
