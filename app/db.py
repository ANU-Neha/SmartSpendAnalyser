from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["SmartSpendDB"]
receipts_collection = db["Receipts"]

def insert_receipt_to_db(user_id, image_path, extracted_text):
    receipt_doc = {
        "user_id": user_id,
        "image_path": image_path,
        "extracted_text": extracted_text,
        "timestamp": datetime.datetime.now()
    }
    receipts_collection.insert_one(receipt_doc)
