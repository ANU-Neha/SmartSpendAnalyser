from .db import insert_receipt_to_db
from flask import Blueprint, request, jsonify
from .ocr_utils import extract_text_from_image
import os

main = Blueprint('main', __name__)

@main.route('/upload', methods=['POST'])
def upload_receipt():
    image = request.files['image']
    user_id = request.form['user_id']

    upload_path = os.path.join('uploads', image.filename)
    image.save(upload_path)

    text = extract_text_from_image(upload_path)

    # Insert to MongoDB
    insert_receipt_to_db(user_id, upload_path, text)

    return jsonify({'message': 'Receipt uploaded and saved.', 'user_id': user_id, 'extracted_text': text})
