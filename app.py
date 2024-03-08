# Main function to run the system with interface setup using Gradio

# Import necessary libraries and functions
import gradio as gr  
from src.question_answering import answer_question # Import function for answering questions


# Define the rules
rules_text = """
## Follow the below rules:
1. Upload a non-empty text document format (.txt).
2. Enter a valid question format (non-word character, no digits, no special symbols) with two or more words in the text box provided.
3. Click the 'Submit' button to get the answer.
"""

# Define the Gradio interface
interface = gr.Interface(
    fn=answer_question,  # Set the function to be executed
    inputs=[
        gr.File(label="Upload Document (.txt)"),
        "text",
    ],  # Define the input components (upload document and text question)
    outputs="text",  # Define the output component (text answer)
    title="Question Answering System",  # Set the title of the interface
    description=rules_text,  # Set the description of the interface
)


# Launch the Gradio interface
interface.launch()
