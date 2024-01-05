from Mongo import questions_collection

def retrieve_questions_by_test(test_id):
    return list(questions_collection.find({"test_id": test_id}))

# Function to retrieve a question by question_id
@staticmethod
def retrieve_question_by_id(question_id):
    return questions_collection.find_one({"_id": question_id})

# Function to insert a new question
@staticmethod
def insert_question(question_data):
    return questions_collection.insert_one(question_data).inserted_id

# Function to update a question
@staticmethod
def update_question(question_id, update_data):
    return questions_collection.update_one({"_id": question_id}, {'$set': update_data})

# Function to delete a question
def delete_question(question_id):
    return questions_collection.delete_one({"_id": question_id}).deleted_count

