from Mongo import sections_collection, tests_collection, questions_collection

# Function to insert a new section
def insert_section(section_data):
    result = sections_collection.insert_one(section_data)
    return result.inserted_id

# Function to update a section
def update_section(section_id, update_data):
    result = sections_collection.update_one({"_id": section_id}, {'$set': update_data})
    return result.modified_count

#Function to retrieve all sections
def retrieve_all_sections():
    return list(sections_collection.find({}))


def retrieve_section_by_id(section_id):
    return sections_collection.find_one({"_id": section_id})

def delete_section_and_related(section_id):
    # Find all tests related to the section
    related_tests = list(tests_collection.find({"section_id": section_id}, {"_id": 1}))
    
    # Delete all questions related to each test
    for test in related_tests:
        questions_collection.delete_many({"test_id": test['_id']})
    
    # Delete all tests related to the section
    tests_deleted = tests_collection.delete_many({"section_id": section_id}).deleted_count
    
    # Finally, delete the section
    section_deleted = sections_collection.delete_one({"_id": section_id}).deleted_count
    
    return {"section_deleted": section_deleted, "tests_deleted": tests_deleted}
