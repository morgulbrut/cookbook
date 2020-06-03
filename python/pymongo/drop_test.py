#!/usr/bin/env python3

import pymongo
from pprint import pprint

client = pymongo.MongoClient("192.168.15.139")
db = client.test

db.reviews.drop()