from pymongo import MongoClient
import json

username = "MONGODB USERNAME"
password = "MONGODB PASSWORD"

client = MongoClient(
    f"mongodb+srv://{username}:{password}@urlshortner.ddysk.mongodb.net/urlshortner?retryWrites=true&w=majority")

db = client.urlshortner
collec = db.urlshortner


def db_insert(doc: dict):
    collec.insert_one(json.loads(json.dumps(doc)))


def db_update(doc: dict):
    collec.find_one_and_replace({'_id': doc['_id']}, doc)
