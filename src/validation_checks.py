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
        return doc_bytes.name.endswith('.txt')
    except AttributeError:
        # Handle the case where the input does not have a 'name' attribute
        return False
