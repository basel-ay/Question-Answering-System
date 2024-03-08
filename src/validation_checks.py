import re


def is_txt_file(doc_bytes):
    """
    Check if the uploaded file is a text file.

    Args:
        doc_bytes (bytes): The document content in bytes.

    Returns:
        bool: True if the file has a .txt extension, False otherwise.
    """
    try:
        # Check if the file name ends with .txt
        return doc_bytes.name.endswith(".txt")
    except AttributeError:
        # Handle the case where the input does not have a 'name' attribute
        return False


def is_question_format(question):
    """
    Validate the format of the question.

    Args:
        question (str): The user's input string.

    Returns:
        bool: True if the input string is a valid question, False otherwise.
    """
    try:
        # Define a regex pattern to match common question structures
        question_pattern = r"^[^\W\d_]+\s+[^\W\d_]+(?:\s+[^\W\d_]+)*\s*(?:\?)?$"


        # Check if the input string matches the question pattern
        if re.match(question_pattern, question.strip()):
            return True
        else:
            return False
    except Exception as e:
        # Handle any errors gracefully and return False
        # print(f"Error validating question format: {e}")
        return False
