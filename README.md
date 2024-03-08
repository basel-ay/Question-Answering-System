# Overview
The Question Answering System is a tool designed to provide answers to user queries based on uploaded text documents and user input questions. It utilizes a pre-trained question-answering model and can also retrieve answers from a database based on similar questions.

## System Design Graph

![System_Graph](https://github.com/basel-ay/Question-Answering-System/assets/64821137/a3cf5fc0-f816-4a9b-b9c8-6130c1fa9b9f)

View graph at Excalidraw: [link](https://excalidraw.com/#json=JfsHGJJcY4_CwG2IpvaYW,29apf2-RjXEH9dwOz0MbwQ)


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
    
    `CREATE TABLE qa_table (
    question TEXT,
    answer TEXT
);`
  
* The .env file should contain the necessary environment variables for database connection.
  
    - `DB_HOST="ENTER_HOST_NAME"`
    - `DB_USER="ENTER_USER_NAME"`
    - `DB_PASSWORD="ENTER_DB_PASSWORD"`
    - `DB_NAME="ENTER_DB_NAME"`
  
* Text preprocessing steps may vary based on specific requirements and language models used.
* Additional error handling and logging can be added as per the application's needs.

## Dependencies

- `gradio==4.20.1`
- `transformers==4.38.2`
- `mysql_connector_repackaged==0.3.1`
- `python-dotenv==1.0.1`
- `os-sys`
- `regex`


## Project Structure and Key Files

![image](https://github.com/basel-ay/Question-Answering-System/assets/64821137/9b25eb27-2db4-4c2e-88ee-4403248cd84f)

## Future Enhancements

#### 1. Multilingual Support
Extend the system's capabilities to support multiple languages beyond Arabic. This enhancement would involve integrating additional pre-trained language models and implementing language detection mechanisms to handle queries in different languages.

#### 2. Interactive Feedback Mechanism
Incorporate an interactive feedback mechanism where users can provide feedback on the accuracy and relevance of the system's answers. This feedback loop can be used to continuously improve the system's performance and refine its underlying models.

#### 3. Summarization
Integrate text summarization techniques to generate concise summaries of the uploaded documents. Summaries can help users quickly grasp the main points of the document and facilitate more efficient question-answering interactions.

#### 4. Customizable Thresholds
Allow users to customize similarity thresholds for question matching and answer retrieval. Providing users with control over these thresholds can accommodate different use cases and preferences, leading to more personalized and accurate responses.

#### 5. Implement more Optimized ways for Similarity Checks for huge data
A more efficient approach for handling large databases is to leverage indexing and optimized search algorithms specifically designed for similarity search. Here's an optimized solution using Locality-Sensitive Hashing (LSH) for approximate nearest neighbor search

#### 6. Graphical User Interface (GUI) Enhancements
Enhance the graphical user interface with interactive visualizations, progress indicators, and real-time updates to improve the user experience. Visual cues and feedback mechanisms can make the system more engaging and intuitive to use.

#### 7. Integration with External Knowledge Sources
Explore integration with external knowledge bases, ontologies, or APIs to enrich the system's knowledge and enhance its ability to provide comprehensive answers to a wide range of questions.

#### 8. Domain-specific Adaptation
Develop mechanisms to adapt the system to specific domains or industries by fine-tuning the underlying models on domain-specific datasets. This adaptation can improve the relevance and accuracy of answers for domain-specific queries.

#### 9. Performance Optimization
Optimize the system's performance by implementing techniques such as caching, parallel processing, and model optimization to reduce response times and resource consumption, especially for large documents or high volumes of concurrent requests.

#### 10. Accessibility Features
Ensure accessibility compliance by incorporating features such as screen reader compatibility, keyboard navigation, and color contrast adjustments to make the system accessible to users with disabilities.

## Sample Images

![image](https://github.com/basel-ay/Question-Answering-System/assets/64821137/e318ebf6-ee91-4a1e-a31c-fda2ee6eae9f)

![image](https://github.com/basel-ay/Question-Answering-System/assets/64821137/8bb6ec92-9406-494a-b7eb-d5148908f883)


