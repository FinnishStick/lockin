from models.threat import Threat
from pymongo import MongoClient
from hashlib import sha256
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["nis2_monitor"]
collection = db["threats"]

def compute_hash(title: str, link: str) -> str:
    to_hash = f"{title}-{link}"
    return sha256(to_hash.encode()).hexdigest()

def save_threat(item: dict):
    # compute unique hash
    item_hash = compute_hash(item["title"], item["link"])
    item["hash"] = item_hash

    # check if already exists
    exists = collection.find_one({"hash": item_hash})
    if exists:
        return False  # duplicate

    # create Threat object with hash as _id
    threat_data = item.copy()
    threat_data["_id"] = item_hash  # use hash as MongoDB _id
    threat = Threat(**threat_data)

    # insert into MongoDB
    collection.insert_one(threat.dict(by_alias=True))
    return True

def get_recent(limit=50):
    cursor = collection.find().sort("published", -1).limit(limit)
    return list(cursor)
