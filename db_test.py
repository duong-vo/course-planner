from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import urllib.parse

# load the environment
load_dotenv(find_dotenv())

# establish mongodb connection
password = os.environ.get('MONGODB_PWD')
connection_string = f"mongodb+srv://vodh2:{urllib.parse.quote(password)}@course.jk30kp4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)

# start playing around
dbs = client.list_database_names()
test_db = client["test"]
collections = test_db.list_collection_names()

def insert_test_doc():
    # insert a test document
    collections = test_db["test"]
    test_document = {
        "name" : "CSE",
        "number": "274"
    }
    inserted_id = collections.insert_one(test_document).inserted_id
    print(inserted_id)

def create_test_documents():
    courses = ["CSE", "MTH", "STA"]
    numbers = ["174", "151", "301"]
    collections = test_db["test"]
    docs = []
    print(zip(courses, numbers))
    for course, number in zip(courses,numbers):
        doc = {"name": course, "number": number}
        docs.append(doc)
    
    collections.insert_many(docs)

def find_all_courses():
    collections = test_db["test"]
    courses = collections.find()
    for course in courses:
        print(course)

find_all_courses()