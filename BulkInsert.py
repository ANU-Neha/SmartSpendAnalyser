import os
from app.ocr_utils import extract_text_from_image
from app.db import insert_receipt_to_db

def bulk_insert_from_folder(folder_path, user_id="kagle_test"):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            image_path = os.path.join(folder_path, filename)
            extracted_text = extract_text_from_image(image_path)
            insert_receipt_to_db(user_id, image_path, extracted_text)
            print(f"Inserted: {filename}")

# Run the function
bulk_insert_from_folder("kagle images", user_id="user_kagle")
