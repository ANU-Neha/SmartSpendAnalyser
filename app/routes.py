from .db import insert_receipt_to_db
from flask import Blueprint, request, jsonify, current_app
from .ocr_utils import extract_text_from_image
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Handles GET requests to the root URL (/).
    Returns a welcome message to indicate the API is operational.
    """
    return jsonify({"message": "Welcome to the Receipt OCR API! Use /upload to post images."}), 200

@main.route('/upload', methods=['POST'])
def upload_receipt():
    """
    Handles POST requests to /upload.
    Expects an image file and an optional user_id to process a receipt.
    """
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    user_id = request.form.get('user_id', 'anonymous') # Use .get for robustness

    if image.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if image:
        # Use the UPLOAD_FOLDER configured in create_app
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image.filename)
        image.save(upload_path)

        text = extract_text_from_image(upload_path)

        # Insert to MongoDB
        insert_receipt_to_db(user_id, upload_path, text)

        return jsonify({'message': 'Receipt uploaded and saved.', 'user_id': user_id, 'extracted_text': text})

    return jsonify({'error': 'Something went wrong during upload'}), 500