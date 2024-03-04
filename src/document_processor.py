# Functions for processing uploaded documents.


def preprocess_document(doc_bytes):
    """
    Function to preprocess the document content.

    Args:
        doc_bytes (str): The path to the document file got from the uploaded file.

    Returns:
        str: The processed document content as a string.
    """
    try:
        # Open the document file and read its content
        with open(doc_bytes, "r") as my_file:
            text = my_file.read()
            # Additional cleaning steps can be added here (optional)

            return text

    except FileNotFoundError:
        # Handle file not found error
        print("Error: File not found.")

        return None

    except Exception as e:
        # Handle any other errors gracefully and return an error message
        print(f"Error: {str(e)}")

        return None
