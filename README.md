<div align="center">
<h1>
Application Judgement Example
</h1>

Built with `asyncflows`

[![main repo](https://img.shields.io/badge/main_repo-1f425f)](https://github.com/asynchronous-flows/asyncflows)
[![Discord](https://img.shields.io/badge/discord-7289da)](https://discord.gg/AGZ6GrcJCh)

![application judgement](https://github.com/asynchronous-flows/application-judgement-example/assets/24586651/304c4b15-b385-4ae5-bce5-16c95e1a680c)

</div>

## Introduction

This flow analyzes an application for a startup accelerator. 

<div align="center">
<img width="955" alt="application judgement" src="https://github.com/asynchronous-flows/application-judgement-example/assets/24586651/6c5b215d-b02f-4ce1-b904-f2088ec7173d">
</div>

## Running the Example

To run the example:

1. Set up [Ollama](https://github.com/asynchronous-flows/asyncflows#setting-up-ollama-for-local-inference) or configure [another language model](https://github.com/asynchronous-flows/asyncflows#using-any-language-model)  

2. Clone the repository

```bash
git clone ssh://git@github.com/asynchronous-flows/application-judgement-example
```

3. Change into the directory

```bash
cd application-judgement-example
```

4. Create and activate your virtual environment (with, for example)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

5. Install the dependencies

```bash
pip install -r requirements.txt
```

Now, either:

### Run the Script

To see output in the terminal, run:

```bash
python application_judgement.py
```

### Run the Gradio App

To start a web interface, run:

```bash
python gradio_app.py
```

## Using your own Data

Replace the contents of `application.txt` and `application_criteria.txt` in the `application_information` folder.

Alternatively, change the contents of the text boxes in the Gradio app.
