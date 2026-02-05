from os import getenv
from pymongo import MongoClient

mongo_uri = getenv("MONGO_URI", "mongodb://localhost:27017/")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")


def get_collection():
    myclient = MongoClient(mongo_uri)
    db = myclient['data']
    collection = db['employees']
    return collection

collection = get_collection()