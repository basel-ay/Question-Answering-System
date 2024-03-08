# Overview
The Question Answering System is a tool designed to provide answers to user queries based on uploaded text documents and user input questions. It utilizes a pre-trained question-answering model and can also retrieve answers from a database based on similar questions.

## System Design Graph

![System_Graph](https://github.com/basel-ay/Question-Answering-System/assets/64821137/a3cf5fc0-f816-4a9b-b9c8-6130c1fa9b9f)

Excalidraw: https://excalidraw.com/#json=JfsHGJJcY4_CwG2IpvaYW,29apf2-RjXEH9dwOz0MbwQ

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

## Dependencies

- `gradio`
- `transformers`
- `mysql-connector-python`
- `dotenv`
- `os-sys`
- `regex`
