#!/usr/bin/env python3
"""
Module 10-update_topics: updates topics of a school document
"""
def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document with given name
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
