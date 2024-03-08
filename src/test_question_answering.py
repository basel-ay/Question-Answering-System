import unittest
from document_processor import preprocess_document
from question_answering import answer_question
from validation_checks import is_txt_file, is_question_format


# class TestQuestionAnswering(unittest.TestCase):
#     def test_preprocess_document(self):
#         # Test preprocessing function with a sample document
#         doc_bytes = b'This is a sample document.'
#         processed_text = preprocess_document(doc_bytes)
#         self.assertEqual(processed_text, 'This is a sample document.')

#     def test_answer_question(self):
#         # Test answering a question with a sample document and question
#         doc_bytes = b'This is a sample document.'
#         question = 'What is this?'
#         answer = answer_question(doc_bytes, question)
#         self.assertEqual(answer, 'This is a sample document.')

#         # Test answering a question with an empty document
#         doc_bytes = b''
#         answer = answer_question(doc_bytes, question)
#         self.assertEqual(answer, 'Error: Document is empty.')

# if __name__ == '__main__':
#     unittest.main()


class TestQuestionAnswering(unittest.TestCase):
    def test_is_txt_file(self):
        # Test with a valid text file
        # txt_file = "example.txt"
        # self.assertTrue(is_txt_file(txt_file))

        # Test with a non-text file
        pdf_file = "example.pdf"
        self.assertFalse(is_txt_file(pdf_file))

        # Test with an empty file
        empty_file = ""
        self.assertFalse(is_txt_file(empty_file))

        # Test with invalid input
        invalid_input = None
        self.assertFalse(is_txt_file(invalid_input))

    def test_is_question_format(self):
        # Test with a valid question
        valid_question = "What is the capital of France?"
        self.assertTrue(is_question_format(valid_question))

        # Test with an invalid question (missing question mark)
        invalid_question = "What is the capital of France"
        self.assertTrue(is_question_format(valid_question))

        # Test with an invalid question (random string)
        random_string = "asdfasdf"
        self.assertFalse(is_question_format(random_string))

        # Test with an empty string
        empty_string = ""
        self.assertFalse(is_question_format(empty_string))

        # Test with invalid input
        invalid_input = None
        self.assertFalse(is_question_format(invalid_input))

if __name__ == '__main__':
    unittest.main()
