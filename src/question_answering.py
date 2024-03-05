# Main logic for answering questions

# Import necessary libraries and modules
from transformers import pipeline
from document_processor import preprocess_document
from database import create_server_connection


pw = "qwerasdf1@"
connection = create_server_connection("localhost", "root", pw, "qa_database")

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

        return answer

    except Exception as e:
        # Handle any errors gracefully and return an error message
        return f"Error: {str(e)}"
