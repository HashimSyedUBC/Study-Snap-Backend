from Mongo import courses_collection, notes_collection # Ensure this is correctly imported from your Mongo setup
from NotesMongo import delete_note_and_related

def insert_course(course_data):
    """Insert a new course into the courses collection."""
    result = courses_collection.insert_one(course_data)
    return result.inserted_id

def update_course(course_id, update_data):
    """Update an existing course in the courses collection."""
    result = courses_collection.update_one({"_id": course_id}, {'$set': update_data})
    return result.modified_count

def retrieve_course_by_id(course_id):
    return courses_collection.find_one({"_id": course_id})

def retrieve_all_courses():
    return list(courses_collection.find({}))

# Function to delete a course, its related notes, sections, tests, and all related questions
def delete_course_and_related(course_id):
    # Find all notes related to the course
    related_notes = list(notes_collection.find({"course_id": course_id}, {"_id": 1}))
    
    # Delete all sections, tests, and questions related to each note
    for note in related_notes:
        delete_note_and_related(note['_id'])
    
    # Finally, delete the course
    course_deleted = courses_collection.delete_one({"_id": course_id}).deleted_count
    
    return {"course_deleted": course_deleted}
