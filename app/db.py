from pymongo import MongoClient
import datetime
import os
from dotenv import load_dotenv # Assuming you'll load dotenv here if not already done

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from environment variables
# For local testing, you can set MONGO_URI="mongodb://localhost:27017/" in your .env
mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
db_name = os.getenv("DB_NAME", "SmartSpendDB") # Allow DB name to be configurable too

client = None # Initialize client to None
try:
    client = MongoClient(mongo_uri)
    # The ping command is cheap and does not require auth.
    # It confirms that the connection is working.
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
    db = client[db_name]
    receipts_collection = db["Receipts"]
except Exception as e:
    print(f"Could not connect to MongoDB: {e}")
    # You might want to exit the application or handle this error more gracefully
    # sys.exit(1) # Uncomment if you want to exit on connection failure

def insert_receipt_to_db(user_id, image_path, extracted_text):
    if client is None:
        print("Cannot insert receipt: MongoDB client is not initialized.")
        return None # Indicate failure

    receipt_doc = {
        "user_id": user_id,
        "image_path": image_path,
        "extracted_text": extracted_text,
        "timestamp": datetime.datetime.utcnow() # Using UTC for consistency
    }
    try:
        result = receipts_collection.insert_one(receipt_doc)
        print(f"Receipt inserted with ID: {result.inserted_id}")
        return result.inserted_id # Return the ID of the inserted document
    except Exception as e:
        print(f"Error inserting receipt: {e}")
        return None # Indicate failure
