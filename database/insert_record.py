import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

def insert_record(record):
    try:

        client = MongoClient(MONGODB_URI)
        db = client[DB_NAME]
        
        collection = db["rover-measurements"]
        
        result = collection.insert_one(record)
        print(f"Rekord został dodany z ID: {result.inserted_id}")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    
    finally:
        client.close()

if __name__ == "__main__":
    with open("../example.json", "r") as file:
        record = json.load(file)
    
    insert_record(record)