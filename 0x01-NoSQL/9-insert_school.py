#!/usr/bin/env python3
"""
Module 9-insert_school: inserts a new document in a collection
"""
def insert_school(mongo_collection, **kwargs):
    """Inserts a new document and returns its _id"""
    return mongo_collection.insert_one(kwargs).inserted_id
