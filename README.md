# Overview
The Question Answering System is a tool designed to provide answers to user queries based on uploaded text documents and user input questions. It utilizes a pre-trained question-answering model and can also retrieve answers from a database based on similar questions.

## System Design Graph

![System_Graph](https://github.com/basel-ay/Question-Answering-System/assets/64821137/a3cf5fc0-f816-4a9b-b9c8-6130c1fa9b9f)

Excalidraw: https://excalidraw.com/#json=JfsHGJJcY4_CwG2IpvaYW,29apf2-RjXEH9dwOz0MbwQ


## Features

- **Text Document Upload**: Users can upload text documents in `.txt` format containing information relevant to their queries. This feature allows users to provide context for their questions and enables the system to generate accurate responses based on the content of the documents.

- **Natural Language Processing**: The system employs state-of-the-art natural language processing (NLP) techniques to analyze both the uploaded documents and the user questions. By leveraging pre-trained language models, it can understand the semantics of the text and extract relevant information to formulate precise answers.

- **Database Integration**: Integration with a MySQL database enhances the system's functionality by enabling it to store and retrieve question-answer pairs. This database serves as a knowledge base, storing previously answered questions and their corresponding answers. This integration improves response accuracy and efficiency, especially for frequently asked questions or similar queries.

- **Question Similarity Detection**: The system incorporates a question similarity detection mechanism to identify similar questions in the database. By comparing the user's question with existing questions stored in the database, it can find the most relevant matches. This feature enhances the user experience by providing consistent and accurate responses to common or related queries.

- **Error Handling**: Comprehensive error handling mechanisms ensure smooth operation and graceful error reporting. The system is equipped to handle various types of errors, including file upload errors, database connection issues, and exceptions during question processing. Error messages are presented in a user-friendly manner, helping users understand and resolve issues effectively.

- **Scalability**: The modular architecture of the system allows for easy scalability and extensibility. New features, such as support for additional languages or integration with different NLP models, can be seamlessly incorporated into the existing framework. This scalability ensures that the system can adapt to evolving user needs and technological advancements.

- **User-Friendly Interface**: The system provides a user-friendly interface that simplifies the process of uploading documents, entering questions, and receiving answers. Clear instructions and intuitive design elements guide users through the interaction process, making it accessible to users with varying levels of technical expertise.



## Project Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/basel-ay/Question-Answering-System.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the MySQL database and configure the environment variables in the `.env` file with your database credentials.
4. 

## Usage Instructions

1. Run the `app.py` script to launch the Gradio interface:

    ```bash
    python app.py
    ```

2. The Gradio interface will open in your default web browser.

3. Upload a non-empty text document (.txt) and enter a valid question format in the provided text box.

4. Click the "Submit" button to get the answer.

Note:
* Ensure that the MySQL database is properly configured with the required table schema (qa_table).
* The .env file should contain the necessary environment variables for database connection.
* Text preprocessing steps may vary based on specific requirements and language models used.
* Additional error handling and logging can be added as per the application's needs.

## Dependencies

- `gradio`
- `transformers`
- `mysql-connector-python`
- `dotenv`
- `os-sys`
- `regex`


## Modules

`question_answering.py`: Contains the core functions for answering questions using AI models and database queries.

`validation_checks.py`: Contains functions for validating uploaded files and question formats.

`document_processor.py`: Contains functions for preprocessing uploaded documents.

`database.py`: Contains functions for establishing connections to a MySQL database.

`test_question_answering.py`: Containing unit tests for functions.


