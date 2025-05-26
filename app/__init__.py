from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables (do this at the module level if you want)
load_dotenv()

# Create the app instance globally
app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Configuration for uploads
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Register blueprints here
from .routes import main
app.register_blueprint(main)

# No create_app function anymore if you go this route
# The 'app' variable is now directly available for gunicorn to find