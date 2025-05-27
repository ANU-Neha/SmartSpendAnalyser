from flask import Blueprint, request, jsonify, current_app
from .ocr_utils import extract_text_from_image
from .db import insert_receipt_to_db # Assuming this is used for uploads
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

# --- NEW ROUTES ADDED BELOW ---

@main.route('/api/charts/bar', methods=['GET'])
def get_bar_chart_data():
    """
    Placeholder for fetching bar chart data.
    Replace with actual logic to query your database and format data.
    """
    # Example placeholder data - replace with your actual data fetching logic
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "datasets": [
            {
                "label": "Monthly Spending",
                "backgroundColor": "rgba(75,192,192,0.4)",
                "borderColor": "rgba(75,192,192,1)",
                "borderWidth": 1,
                "hoverBackgroundColor": "rgba(75,192,192,0.6)",
                "hoverBorderColor": "rgba(75,192,192,1)",
                "data": [65, 59, 80, 81, 56, 70] # Example spending amounts
            }
        ]
    }
    return jsonify(data), 200

@main.route('/api/charts/pie', methods=['GET'])
def get_pie_chart_data():
    """
    Placeholder for fetching pie chart data.
    Replace with actual logic to query your database and format data.
    """
    # Example placeholder data - replace with your actual data fetching logic
    data = {
        "labels": ["Groceries", "Utilities", "Transport", "Entertainment", "Other"],
        "datasets": [
            {
                "data": [300, 50, 100, 75, 120], # Example spending amounts by category
                "backgroundColor": [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#4BC0C0",
                    "#9966FF"
                ],
                "hoverBackgroundColor": [
                    "#FF6384",
                    "#36A2EB",
                    "#FFCE56",
                    "#4BC0C0",
                    "#9966FF"
                ]
            }
        ]
    }
    return jsonify(data), 200

@main.route('/api/summary', methods=['GET'])
def get_summary_data():
    """
    Placeholder for fetching spending summary data.
    Replace with actual logic to query your database and calculate summary.
    """
    # Example placeholder data - replace with your actual data fetching logic
    summary_data = {
        "currentMonthSpending": 1250.75,
        "lastMonthSpending": 1100.50,
        "averageDaily": 45.25,
        "savingsRate": 15 # Example percentage
    }
    return jsonify(summary_data), 200

@main.route('/api/transactions', methods=['GET'])
def get_transactions_data():
    """
    Placeholder for fetching recent transactions.
    Replace with actual logic to query your database for transactions.
    """
    # Example placeholder data - replace with your actual data fetching logic
    transactions_list = [
        {"id": "t1", "store": "SuperMart", "amount": 55.20, "date": "2024-05-25"},
        {"id": "t2", "store": "Cafe Latte", "amount": 12.50, "date": "2024-05-24"},
        {"id": "t3", "store": "Gas Station", "amount": 40.00, "date": "2024-05-23"},
        {"id": "t4", "store": "Bookstore", "amount": 22.80, "date": "2024-05-22"},
        {"id": "t5", "store": "Restaurant", "amount": 75.00, "date": "2024-05-21"}
    ]
    return jsonify(transactions_list), 200