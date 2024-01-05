from Mongo import tests_collection
from Mongo import questions_collection

# Function to insert a new test
def insert_test(test_data):
    result = tests_collection.insert_one(test_data)
    return result.inserted_id

# Function to update a test
def update_test(test_id, update_data):
    result = tests_collection.update_one({"_id": test_id}, {'$set': update_data})
    return result.modified_count

# Function to retrieve a test by test_id
def retrieve_test_by_id(test_id):
    return tests_collection.find_one({"_id": test_id})

# Function to retrieve all tests
def retrieve_all_tests():
    return list(tests_collection.find())

def delete_test_and_questions(test_id):
    questions_deleted = questions_collection.delete_many({"test_id": test_id}).deleted_count
    test_deleted = tests_collection.delete_one({"_id": test_id}).deleted_count
    return {"test_deleted": test_deleted, "questions_deleted": questions_deleted}

