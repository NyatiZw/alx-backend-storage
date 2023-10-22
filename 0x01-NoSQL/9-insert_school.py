#!/usr/bin/env python3

from pymongo.collection import Collection
from pymongo import InsertOne


def insert_school(mongo_collection, **kwargs):
    try:
        document = kwrgs

        result = mongo_collection.bulk_write([InsertOne(document)])
        new_id = result.inserted_ids[0]
        return str(new_id)
    except Exception as e:
        return None
