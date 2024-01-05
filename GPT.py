import os
from openai import OpenAI
# Initialize the OpenAI client with your API key
api_key = os.getenv('API_KEY')

client = OpenAI(api_key=api_key)

def notes(scraped_content):
    notes = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "generate me a summary given lecture content. return formatted markdown with a title and subtopics. MUST BE CONSISTENT. USE BULLET POINTS DO NOT SKIP ANY CONTENT. COVER AS MUCH AS POSSILBE WHILE BEING CONCISE"},
        {"role": "user", "content": scraped_content}
        ]
    )
    return notes.choices[0].message.content

def questions(cleaned_content):
    questions = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "generate 10 multiple choice questions and answers. MUST RETURN EVERY QUESTION IN FORMAT Q: EXAMPLE, OPTIONS: A,B,C,D, ANSWER: A"},
            {"role": "user", "content": cleaned_content}
        ]
    )
    return questions.choices[0].message.content