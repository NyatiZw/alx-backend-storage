#!/usr/bin/env python3
"""This is a script for listing all documents"""


from pymongo.collection import Collection


def list_all(mongo_collection):
    try:
        documents = list(mongo_collection.find({}))
        return documents
    except Exception as e:
        print("{e}")
        return []
