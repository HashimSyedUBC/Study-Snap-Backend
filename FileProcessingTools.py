import slate3k as slate
from bson import binary
import GPT as gpt
from Classes import Course, 

def convert_pdf_to_text(file_path):
    with open(file_path, 'rb') as f:
        doc = slate.PDF(f)

    clean_string = ""
    for item in doc:
        # Replace special characters with an empty string or space as needed
        item = item.replace('\t', '')  # Remove tabs
        item = item.replace('\r', '')  # Remove carriage returns
        item = item.replace('\xa0', ' ')  # Replace non-breaking spaces with a normal space
        item = item.replace('\u202f', ' ')  # Replace narrow no-break spaces with a normal space

        # Append the cleaned item to the clean_string
        clean_string += item
    
    return clean_string

def convert_to_markdown_to_binary(file_name,content):
    with open(f"{file_name}.md", "w") as file:
        file.write(content)
    # Step 2: Read the markdown file in binary mode and store the content
    with open(f"{file_name}.md", "rb") as file:
        binary_content = binary.Binary(file.read())
    
    return file_name, binary_content


def make_notes(file_list):
    for file in file_list:
        content = convert_pdf_to_text(file)
        notes = gpt.notes(content)
    return 

def make_questions(file_list):
    for file in file_list:
        content = convert_pdf_to_text(file)
        notes = gpt.notes(content)

        

def create_course(file_list, coursename, course year, university):
    