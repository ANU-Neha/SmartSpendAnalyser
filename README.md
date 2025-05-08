# SmartSpend Analyzer

SmartSpend Analyzer is an OCR-based system designed to extract text from receipt images, process the extracted data, and store it in MongoDB for further analysis and visualization. The project is built using Flask, Python, MongoDB, and Tesseract OCR.

---

## Tech Stack

- **Python**: Primary programming language for backend and OCR functionality.
- **Flask**: Web framework used for building the backend API.
- **MongoDB**: NoSQL database used for storing extracted receipt data.
- **Tesseract OCR**: Optical Character Recognition (OCR) tool used to extract text from receipt images.
- **Pymongo**: Python library for interacting with MongoDB.

---

## Project Overview

This project aims to streamline the process of extracting, storing, and analyzing receipt data. It includes the following features:
- Uploading receipt images via an API.
- Extracting text from the images using Tesseract OCR.
- Storing the extracted data in MongoDB.
- The possibility of connecting this backend to a frontend (to be developed by Anjitha).

---

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/ANU-Neha/SmartSpendAnalyser.git
cd SmartSpendAnalyser

2. Create a Virtual Environment
It's best to create a virtual environment to manage project dependencies:

bash
Copy code
python3 -m venv myenv
3. Activate the Virtual Environment
Activate the virtual environment to install the necessary dependencies:

On Mac/Linux:

bash
Copy code
source myenv/bin/activate
On Windows:

bash
Copy code
myenv\Scripts\activate
4. Install Dependencies
Install the required libraries using requirements.txt:

bash
Copy code
pip install -r requirements.txt
5. Set Up MongoDB
Make sure MongoDB is running locally on your machine. If you're using Docker or the MongoDB community edition, you can start it as follows:

bash
Copy code
mongod
6. Run the Flask Application
Run the Flask app to start the server:

bash
Copy code
python Run.py
This will start the application on http://127.0.0.1:5000. You can test it by making requests to the API.

7. Optional: Insert Sample Receipt Data
To insert sample receipt data into the database, you can use the bulk_insert.py script. It will process all images in the provided folder and store the extracted data in MongoDB.

Run the following command:

bash
Copy code
python bulk_insert.py
Make sure the receipt images are in the kagle images folder (or another folder you specify).

API Endpoints
1. POST /upload
This endpoint allows you to upload receipt images for OCR processing and data extraction.

Request Body:

image: (form-data) The receipt image file to be uploaded.

user_id: (form-data) A unique identifier for the user uploading the receipt.

Example (using Postman or CURL):

bash
Copy code
curl -X POST -F "image=@path_to_receipt.jpg" -F "user_id=user_test" http://127.0.0.1:5000/upload
Response:

Status: 200 OK

Body: The extracted text from the receipt, along with the user ID.

Example:

json
Copy code
{
  "user_id": "user_test",
  "extracted_text": "Receipt details will be here..."
}
Running the Application
After setting up the project and starting the Flask app, you can upload receipt images via Postman or any HTTP client. The backend will extract text from the uploaded images using Tesseract OCR, store the data in MongoDB, and return the extracted text in the response.

Folder Structure
Here is an overview of the folder structure:

graphql
Copy code
SmartSpendAnalyser/
│
├── app/                     # Main application folder
│   ├── __init__.py          # Initializes the app
│   ├── db.py                # MongoDB connection and functions
│   ├── ocr_utils.py         # Functions related to OCR (Tesseract)
│   └── routes.py            # Routes and endpoints for the API
│
├── kagle images/            # Folder containing receipt images for bulk insertion
│
├── Run.py                   # Main entry point to run the app
├── bulk_insert.py           # Script for inserting receipt data in bulk
├── requirements.txt         # Python dependencies
├── README.md                # This file
└── myenv/                   # Virtual environment folder


Contributing
We welcome contributions to the SmartSpend Analyzer project! If you have suggestions or improvements, please feel free to open an issue or submit a pull request.

To contribute:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Make your changes and commit them (git commit -am 'Add new feature').

Push the changes (git push origin feature-branch).

Open a pull request to merge your changes into the main branch.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Final Notes
This is a backend-focused project. The frontend (developed by Anjitha) will be connected later.

To test the OCR functionality, make sure you have the necessary receipt images and that Tesseract OCR is installed.

This README file serves as a comprehensive guide for your teammates to set up and run the project.


