#!/usr/bin/env python3
"""This is a script for listing all documents"""


from pymongo.collection import Collection
from pymongo import MongoClient


def list_all(mongo_collection):
    try:
        documents = list(mongo_collection.find({}))
        return documents
    except Exception as e:
        return []
