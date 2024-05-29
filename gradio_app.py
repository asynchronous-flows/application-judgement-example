import os

from pathlib import Path

import gradio as gr

import asyncio

import pandas as pd
from asyncflows import AsyncFlows
from asyncflows.utils.async_utils import merge_iterators

from asyncflows.log_config import get_logger

application_text_path = os.path.join("application_information", "application.txt")
application_criteria_path = os.path.join("application_information", "application_criteria.txt")

if os.path.exists(application_text_path):
    with open(application_text_path, "r") as f:
        default_application_text = f.read()
else:
    default_application_text = ""


if os.path.exists(application_criteria_path):
    with open(application_criteria_path, "r") as f:
        default_application_criteria = f.read()
else:
    default_application_criteria = ""


with gr.Blocks() as demo:
    with gr.Accordion(label="Inputs"):
        with gr.Row():
            application = gr.Textbox(default_application_text, label="Application text", placeholder="Please provide the application text")
            criteria = gr.Textbox(default_application_criteria, label="Application criteria", placeholder="Please provide the application criteria")

    submit_button = gr.Button("Submit")

    with gr.Row():
        judgement = gr.Textbox(label="Judgement", interactive=False)
        suggestions = gr.Textbox(label="Suggestions", interactive=False)

    async def handle_submit(application_text, criteria):
        # Clear the output fields
        yield {
            judgement: "",
            suggestions: "",
        }

        # Load the chatbot flow
        flow = AsyncFlows.from_file("application_judgement.yaml").set_vars(
            application=application_text,
            application_criteria=criteria,
        )

        async for outputs in flow.stream("judgement.result"):
            yield {
                judgement: outputs
            }

        async for outputs in flow.stream("suggestions.result"):
            yield {
                suggestions: outputs
            }


    submit_button.click(
        fn=handle_submit,
        inputs=[
            application,
            criteria,
        ],
        outputs=[
            judgement,
            suggestions,
        ],
    )


if __name__ == "__main__":
    demo.launch()
