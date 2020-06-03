#!/usr/bin/env python3

import pymongo
from pprint import pprint

query = {"cuisine":"Pizza", "rating":5}

client = pymongo.MongoClient("192.168.15.139")
db = client.test

collection = db['reviews']
cursor = collection.find(query)
for document in cursor:
    pprint(document)
print("Found {} entries".format(collection.count_documents(query)))

