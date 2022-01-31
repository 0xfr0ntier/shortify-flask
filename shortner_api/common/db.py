from pymongo import MongoClient
import json

client = MongoClient(
    "mongodb+srv://kaneki:hV2pThgF9fjETTN9@urlshortner.ddysk.mongodb.net/urlshortner?retryWrites=true&w=majority")

db = client.urlshortner
collec = db.urlshortner


def db_insert(doc: dict):
    collec.insert_one(json.loads(json.dumps(doc)))


def db_update(doc: dict):
    collec.find_one_and_replace({'_id': doc['_id']}, doc)