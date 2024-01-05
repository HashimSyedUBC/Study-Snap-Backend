import os
from openai import OpenAI
import slate3k as slate

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="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")

def generate_summary_and_save(file_path, output_path):
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

    notes = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "generate me a summary given lecture content. return formatted markdown with a title and subtopics. MUST BE CONSISTENT. USE BULLET POINTS DO NOT SKIP ANY CONTENT. COVER AS MUCH AS POSSILBE WHILE BEING CONCISE"},
            {"role": "user", "content": clean_string}
        ]
    )

    questions = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "generate 10 multiple choice questions and answers. MUST RETURN EVERY QUESTION IN FORMAT Q: EXAMPLE, OPTIONS: A,B,C,D, ANSWER: A"},
            {"role": "user", "content": clean_string}
        ]
    )

    summary_content = notes.choices[0].message.content
    question_content = questions.choices[0].message.content


    # Save the summary content to a Markdown file
    with open(output_path + "_notes.md", 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(summary_content)
    with open(output_path + "_questions.md", 'w', encoding='utf-8') as markdown_file:
        markdown_file.write(question_content)
    



# Specify the directory path where your lecture files are located
lecture_directory = 'Phil220'

# Specify the directory where you want to store the summary files
summary_directory = 'Phil220_Summaries'

# Create the summary directory if it doesn't exist
os.makedirs(summary_directory, exist_ok=True)

# List all PDF files in the lecture directory
lecture_files = [f for f in os.listdir(lecture_directory) if f.endswith('.pdf')]

# Loop through each lecture file and generate summaries
for file_name in lecture_files:
    file_path = os.path.join(lecture_directory, file_name)
    output_file_name = os.path.splitext(file_name)[0]
    output_path = os.path.join(summary_directory, output_file_name)  # Create a summary file in the summary directory
    generate_summary_and_save(file_path, output_path)