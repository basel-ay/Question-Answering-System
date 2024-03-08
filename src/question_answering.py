# Main logic for answering questions

# Import necessary libraries and modules
from transformers import pipeline

from src.document_processor import preprocess_document
from src.validation_checks import is_txt_file, is_question_format
from src.database import create_server_connection

import os
from dotenv import load_dotenv
import difflib

# Load environment variables from .env file
load_dotenv()

# Get the database variables from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Establish the connection to the database
connection = create_server_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

# Load the pre-trained question answering model
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")  # For Arabic language

def find_similar_question(input_question):
    """
    Find the most similar question in the database to the input question.

    Args:
        input_question (str): The user's input question.

    Returns:
        str or None: The most similar question found in the database, or None if no similar question is found.
    """
    try:
        # Query the database to retrieve questions
        all_questions = retrieve_all_questions_from_database()

        # Find the most similar question using difflib
        most_similar_question = difflib.get_close_matches(input_question, all_questions, n=1)

        # If the similarity ratio exceeds a threshold, return the most similar question
        if (
            most_similar_question and difflib.SequenceMatcher(None, input_question, most_similar_question[0]).ratio() > 0.85
        ):
            return most_similar_question[0]
        else:
            return None
    except Exception as e:
        # Handle any errors gracefully and return None
        # print(f"Error finding similar question: {e}")
        return f"Error finding similar question: {e}"


# Function to retrieve all questions from the database
def retrieve_all_questions_from_database():
    """
    Retrieve all questions stored in the database.

    Returns:
        list: A list of all questions stored in the database.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT question FROM qa_table")
        questions = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return questions
    except Exception as e:
        # Handle any errors gracefully and return an empty list
        # print(f"Error retrieving questions from database: {e}")
        return f"Error retrieving questions from database: {e}"


# Function to retrieve answer from the database
def retrieve_answer_from_database(question):
    """
    Retrieve the answer corresponding to a given question from the database.

    Args:
        question (str): The question to retrieve the answer for.

    Returns:
        str: The answer to the given question.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT answer FROM qa_table WHERE question = %s", (question,))
        answer = cursor.fetchone()[0]
        cursor.close()
        return answer
    except Exception as e:
        # Handle any errors gracefully and return None
        # print(f"Error retrieving answer from database: {e}")
        return f"Error retrieving answer from database: {e}"


def answer_using_ai_model(context, question):
    """
    Answer a question using a pre-trained question answering model and store the new question-answer pair in the database.

    Args:
        context (str): The document context for answering the question.
        question (str): The question to be answered.

    Returns:
        str: The answer to the given question.
    """
    try:
        answer = qa_model(question=question, context=context)["answer"]
        # Store the new question-answer pair in the database
        db_cursor = connection.cursor()
        db_cursor.execute("INSERT INTO qa_table (question, answer) VALUES (%s, %s)", (question, answer))
        connection.commit()
        return answer
    except Exception as e:
        # Handle any errors gracefully and return None
        # print(f"Error answering question using AI model: {e}")
        return f"Error answering question using AI model: {e}"


def answer_question(doc_bytes, question):
    """
    Answer a question using a pre-trained AI model and/or the database.

    Args:
        doc_bytes (bytes): The document content in bytes.
        question (str): The question to be answered.

    Returns:
        str: The answer to the given question.
    """
    try:
        # Check if the uploaded file is a text file
        if not is_txt_file(doc_bytes):
            return "Please upload a text file."
        
        # Check if a question is provided
        if not question.strip():
            return "Please enter a question."
        
        # Validate the format of the question.
        if not is_question_format(question):
            return "Please enter a valid question format."
        
        # Preprocess the document content
        context = preprocess_document(doc_bytes)

        # Check for similar questions in the database
        similar_question = find_similar_question(question)

        if similar_question is not None:
            # Retrieve the corresponding answer from the database
            answer = retrieve_answer_from_database(similar_question)
        else:
            # Answer the question using the AI model
            answer = answer_using_ai_model(context, question)

        return answer

    except Exception as e:
        # Handle any errors gracefully and return an error message
        # print(f"Error answering question: {e}")
        return f"Error: Failed to answer the question {e}"
