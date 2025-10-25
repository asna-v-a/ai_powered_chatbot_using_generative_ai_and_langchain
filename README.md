# AI-Powered Chatbot using Generative AI and LangChain

## Overview
This project is an **AI-powered chatbot** built using **Generative AI** and **LangChain**, capable of understanding documents and answering user questions in real time. It combines language models, vector search, and conversation memory to build intelligent conversational systems.

## Features
- Conversational AI with contextual understanding.
- Document-based question answering using embeddings and vector search.
- Maintains conversation context across multiple interactions.
- Modular structure for easy extension.

## Project Structure

ai_powered_chatbot_using_generative_ai_and_langchain/
│
├── 1-langchain_basics/                # Core LangChain scripts and examples
│   ├── chatbot.py                      # Basic chatbot implementation
│   ├── qachatbot.py                    # Document-based Q&A chatbot
│   ├── tools.ipynb                     # Experimentation with LangChain tools
│   └── langchain_basics.ipynb          # Tutorials and experiments
│
├── main.py                             # Entry point to run chatbot
├── requirements.txt                    # Python dependencies
├── pyproject.toml                       # Project configuration
├── README.md                            # Project documentation
├── .python-version                      # Python version used
├── .env                                 # Environment variables (API keys)
├── .gitignore                           # Ignore environment, secrets, etc.
└── uv.lock                              # Dependency lock file


## Installation
1. **Clone the repository**
```bash
git clone https://github.com/asna-v-a/ai_powered_chatbot_using_generative_ai_and_langchain.git
cd ai_powered_chatbot_using_generative_ai_and_langchain
```
2. **Set up a virtual environment (optional)**

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```
3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a .env file in 1-langchain_basics/:

```ini
OPENAI_API_KEY=your_openai_api_key
```

**Usage**
Run the chatbot

```bash
python main.py
```
Experiment with LangChain tools

```bash
jupyter notebook langchain_basics.ipynb
jupyter notebook tools.ipynb
```

## Technologies Used

Python 3.12

LangChain

OpenAI API

Streamlit (optional)

Jupyter Notebook

## Notes

Never commit secrets such as API keys. Use .env files and .gitignore.

This project is for learning and experimentation with AI chatbots.
