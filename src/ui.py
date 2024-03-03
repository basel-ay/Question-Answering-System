# User interface setup using Gradio

import gradio as gr
from document_processor import upload_document, process_document
from question_answering import answer_question


interface = gr.Interface(
    fn=answer_question,
    inputs=[gr.File(label="Upload Document"), "text"],
    outputs="text",
    title="Question Answering System",
)
interface.launch()
