from dotenv import load_dotenv
import os
from firebase_admin import credentials, initialize_app, firestore

# Load environment variables from the .env file
load_dotenv()

# Load the credentials
cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")
if cred_path:
    cred = credentials.Certificate(cred_path)
    initialize_app(cred)
else:
    raise ValueError("Firebase credentials path not found in environment variables.")

# Firestore database instance
db = firestore.client()
