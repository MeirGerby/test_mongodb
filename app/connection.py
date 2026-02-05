from os import getenv
from pymongo import MongoClient

mongo_uri = getenv("MONGO_URI", "api")

def get_collection():
    myclient = MongoClient(mongo_uri)
    db = myclient['data']
    collection = db['employees']
    return collection

collection = get_collection()