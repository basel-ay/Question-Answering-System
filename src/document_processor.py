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
        with open(doc_bytes, "r", encoding="utf-8") as my_file:
            # Read the content of the file
            text = my_file.read()

            # Additional cleaning steps can be added here

            # Replace non-printable characters with space
            raw_text = ''.join(char if char.isprintable() else ' ' for char in text)

            return raw_text

    except FileNotFoundError:
        # Handle file not found error
        return "Error: File not found."

    except Exception as e:
        # Handle any other errors gracefully and return an error message
        return f"Error: {str(e)}"
