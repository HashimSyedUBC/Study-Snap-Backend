from Mongo import notes_collection, sections_collection  # Ensure this is correctly imported from your Mongo setup
from SectionsMongo import delete_section_and_related

def insert_note(note_data):
    result = notes_collection.insert_one(note_data)
    return result.inserted_id

def update_note(note_id, update_data):
    result = notes_collection.update_one({"_id": note_id}, {'$set': update_data})
    return result.modified_count


# Function to retrieve a note by its ID
def retrieve_note_by_id(note_id):
    return notes_collection.find_one({"_id": note_id})

# Function to retrieve all notes
def retrieve_all_notes():
    return list(notes_collection.find({}))

# Function to delete a note, its related sections, tests, and all related questions
def delete_note_and_related(note_id):
    # Find all sections related to the note
    related_sections = list(sections_collection.find({"note_id": note_id}, {"_id": 1}))
    
    # Delete all tests and questions related to each section
    for section in related_sections:
        delete_section_and_related(section['_id'])
    
    # Finally, delete the note
    note_deleted = notes_collection.delete_one({"_id": note_id}).deleted_count
    
    return {"note_deleted": note_deleted}
