from flask import Flask
from flask_cors import CORS # Import CORS
import os
from dotenv import load_dotenv # Import load_dotenv

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    app = Flask(__name__)
    CORS(app) # Enable CORS for all routes

    # Configuration for uploads
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from .routes import main
    app.register_blueprint(main)

    return app