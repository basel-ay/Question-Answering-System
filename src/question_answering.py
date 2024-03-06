# Main logic for answering questions

# Import necessary libraries and modules
from transformers import pipeline
from src.document_processor import preprocess_document
from src.database import create_server_connection
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get the database variables from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Stablish the connection to the database
connection = create_server_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

# Load the pre-trained question answering model
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2")  # For Arabic language


def answer_question(doc_bytes, question):
    """
    Function to answer a question using a pre-trained question answering model.

    Parameters:
    - doc_bytes: bytes, the document content in bytes
    - question: str, the question to be answered

    Returns:
    - answer: str, the answer to the question
    """
    try:
        # Preprocess the document content
        context = preprocess_document(doc_bytes)

        # Check if the question is in the database
        db_cursor = connection.cursor()
        db_cursor.execute(
            "SELECT answer FROM qa_table WHERE question = %s", (question,)
        )
        result = db_cursor.fetchone()
        if result:
            return result[0]  # If found in the database, return the answer

        # If not found in the database, use the AI model to answer the question
        # Use the pre-trained question answering model to answer the question
        answer = qa_model(question=question, context=context)["answer"]

        # Store the new question-answer pair in the database
        db_cursor.execute("INSERT INTO qa_table (question, answer) VALUES (%s, %s)", (question, answer))
        connection.commit()

        return answer

    except Exception as e:
        # Handle any errors gracefully and return an error message
        return f"Error: {str(e)}"
