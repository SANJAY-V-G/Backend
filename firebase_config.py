import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_firebase():
    try:
        if not firebase_admin._apps:
            print("[INFO] Firebase not initialized. Initializing now...")
            cred_path = "firebase-creds.json"

            if not os.path.exists(cred_path):
                raise FileNotFoundError(f"[ERROR] Credentials file '{cred_path}' not found.")

            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
            print("[SUCCESS] Firebase initialized successfully.")
        else:
            print("[INFO] Firebase already initialized.")

        db = firestore.client()
        print("[SUCCESS] Firestore client obtained.")
        return db

    except Exception as e:
        print(f"[EXCEPTION] Firebase initialization failed: {e}")
        return None

# Example usage
if __name__ == "__main__":
    db = initialize_firebase()
    if db:
        print("[STATUS] Firestore is ready to use.")
    else:
        print("[STATUS] Failed to initialize Firestore.")