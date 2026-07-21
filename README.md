# LLM Applications using Google Gemini

## Project Overview

This repository contains four Python applications demonstrating different Large Language Model (LLM) concepts using Google Gemini API.

The project covers:

- LLM Workflow
- Prompt Chaining
- Agentic AI
- Retrieval-Augmented Generation (RAG)

These applications are developed as part of an academic assignment to understand practical implementations of Generative AI.

---

# Project Structure

```
LLM_Assignment/
│
├── Q1_LLM_Workflow/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── README.md
│
├── Q2_Prompt_Chaining/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── README.md
│
├── Q3_Agentic_AI/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── README.md
│
├── Q4_RAG/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   ├── data/
│   │   └── sample.pdf
│   └── README.md
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# Technologies Used

- Python 3.10+
- Google Gemini API
- LangChain
- FAISS
- PyPDF
- Python Dotenv

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/LLM_Assignment.git
```

Move into the project directory

```bash
cd LLM_Assignment
```

Install the dependencies

```bash
pip install -r requirements.txt
```

---

# Configure API Key

Create a file named `.env`

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Replace the API key with your own Google Gemini API key.

---

# Running the Projects

## Q1 - LLM Workflow

```bash
cd Q1_LLM_Workflow
python app.py
```

The application accepts user input and generates responses using Google Gemini.

---

## Q2 - Prompt Chaining

```bash
cd Q2_Prompt_Chaining
python app.py
```

Workflow:

1. Generate Summary
2. Extract Key Points
3. Generate Three Questions

---

## Q3 - Agentic AI

```bash
cd Q3_Agentic_AI
python app.py
```

Workflow:

- Accept Task
- Plan Steps
- Execute Plan
- Display Final Result

---

## Q4 - RAG Based Question Answering

Place a PDF inside

```
Q4_RAG/data/
```

Run

```bash
cd Q4_RAG
python app.py
```

The application

- Loads the PDF
- Splits the document into chunks
- Retrieves relevant information
- Sends context to Gemini
- Displays the final answer

---

# Required Libraries

```
google-generativeai
langchain
langchain-community
langchain-google-genai
faiss-cpu
pypdf
python-dotenv
```

---

# Learning Outcomes

After completing this project, you will understand:

- Working with Large Language Models
- Prompt Engineering
- Prompt Chaining
- Agentic AI
- Retrieval-Augmented Generation (RAG)
- Document Retrieval
- Google Gemini API Integration

---

# Sample Outputs

### Q1

```
User:
What is Artificial Intelligence?

AI is the simulation of human intelligence by machines.
```

### Q2

```
Summary Generated

↓

Key Points Extracted

↓

Three Questions Generated
```

### Q3

```
Task

↓

Planning

↓

Execution

↓

Final Solution
```

### Q4

```
PDF

↓

Chunking

↓

Retrieval

↓

LLM

↓

Answer
```

---

# Future Improvements

- Multi-document RAG
- Vector databases (FAISS/ChromaDB)
- Memory-enabled AI Agents
- Streamlit Web Interface
- Voice-based AI Assistant
- Chat History Support

---

# Author

**Kuchu Chaithanya**

Cyber Security Department

Mallareddy University

---

# License

This project is developed for educational and academic purposes.
