from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the MongoDB connection string from the environment variable
mongodb_uri = os.getenv("MONGODB_URI")

# Connect to MongoDB
client = MongoClient(mongodb_uri)

# Access the 'Tutor-App' database
tutor_app_db = client['Tutor-App']

# Accessing the collections
courses_collection = tutor_app_db['Courses']
notes_collection = tutor_app_db['Notes']
questions_collection = tutor_app_db['Questions']
sections_collection = tutor_app_db['Sections']
tests_collection = tutor_app_db['Tests']
user_collection = tutor_app_db['User']
