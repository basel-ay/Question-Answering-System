# Main logic for answering questions

# Import necessary libraries and modules
from transformers import pipeline
from document_processor import preprocess_document


# Load the pre-trained question answering model
qa_model = pipeline("question-answering", model="deepset/roberta-base-squad2") # For Arabic language


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

        # Use the pre-trained question answering model to answer the question
        answer = qa_model(question=question, context=context)["answer"]

        return answer
    except Exception as e:
        # Handle any errors gracefully and return an error message
        return f"Error: {str(e)}"
