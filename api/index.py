# api/index.py
# This file lets Vercel load your existing Flask app as a serverless function.

from app import app  # assumes `app = Flask(__name__)` is defined in app.py
