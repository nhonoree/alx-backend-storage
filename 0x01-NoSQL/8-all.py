#!/usr/bin/env python3
"""
Module 8-all: lists all documents in a collection
"""
def list_all(mongo_collection):
    """Lists all documents in the given collection"""
    return list(mongo_collection.find())
