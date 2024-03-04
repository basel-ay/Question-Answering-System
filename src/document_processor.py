# Functions for processing uploaded documents.

import PyPDF2  # Or appropriate library for your document formats.


def preprocess_document(doc_bytes):
    """
    Args:
        :param doc_bytes: The document to be processed.

    Returns:
        :rtype: str
    """
    # Handle document format (text file: decode, PDF: extract text)
    if doc_bytes.startswith(b"%PDF"):
        pdf_reader = PyPDF2.PdfReader(doc_bytes)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    else:
        text = doc_bytes.decode("utf-8")
    # Additional cleaning steps (optional)
    return text
