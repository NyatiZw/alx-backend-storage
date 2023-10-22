#!/usr/bin/env python3
"""This is a script for listing all documents"""

from pymongo import Collection

def list_all(mongo_collection: Collection):
    """Lists all documents in the given collection

    Args:
        mongo_collection (pymongo.collection.Collection): Collection

    Returns:
        list: List of documents
    """
    try:
        documents = list(mongo_collection.find({}))
        return documents
    expect Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
