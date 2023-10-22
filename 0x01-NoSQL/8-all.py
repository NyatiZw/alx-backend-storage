#!/usr/bin/env python3
"""This is a script for listing all documents"""


from pymongo import MongoClient


def list_all(mongo_collection):
    client = MongoClient("localhost", 27017, maxPoolSize=50)
    db = client.localhost
    collection = db['chain']
    cursor = collection.find({})
    for document in cursor:
        print(document)


if __name__ == '__main__':
    pass
