# Main function to run the system with interface setup using Gradio

# Import necessary libraries and functions
import gradio as gr  
from src.question_answering import answer_question # Import function for answering questions

# Define the Gradio interface
interface = gr.Interface(
    fn=answer_question,  # Set the function to be executed
    inputs=[
        gr.File(label="Upload Document (.txt)"),
        "text",
    ],  # Define the input components (upload document and text question)
    outputs="text",  # Define the output component (text answer)
    title="Question Answering System",  # Set the title of the interface
)


# Launch the Gradio interface
interface.launch()
