#!/usr/bin/env python3

import pymongo
from pprint import pprint
import json

if __name__ == '__main__':
    client = pymongo.MongoClient("192.168.0.17")

    for db in client.list_database_names():
        for collection in client[db].list_collection_names():
            print("\n=========================\n",db,collection,"\n=========================\n")
            cursor = client[db][collection].find({})
            for document in cursor:
                pprint(document)
            