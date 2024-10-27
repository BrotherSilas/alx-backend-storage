#!/usr/bin/env python3
"""
Returns students sorted by average score from the MongoDB collection.
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
    - mongo_collection: The pymongo collection object containing student data.

    Returns:
    - A list of students with an added field `averageScore`, sorted by this field.
    """
    students = mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return list(students)
