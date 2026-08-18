# 🤖 RAG Question Answering System using LangChain, Gemini & FAISS

## 📌 About the Project

This project is a Retrieval-Augmented Generation (RAG) based Question Answering System built using Python, LangChain, Google Gemini, Gemini Embeddings, and FAISS.

The system loads a document, splits it into smaller chunks, converts the chunks into embeddings, stores them in a FAISS vector database, retrieves relevant information, and uses Gemini to generate the final answer.

## 🎯 Objective

The main objective is to build a simple RAG system that can answer questions based on information available in a given document.

## 🛠️ Technologies Used

- Python
- LangChain
- Google Gemini
- Gemini Embeddings
- FAISS
- Vector Similarity Search
- VS Code
- Git & GitHub

## 🔄 RAG Workflow

Document → Text Loader → Text Chunking → Gemini Embeddings → FAISS Vector Database → User Query → Similarity Search → Relevant Chunks → Gemini LLM → Final Answer

## ✨ Features

- Loads text documents
- Splits documents into smaller chunks
- Generates Gemini embeddings
- Stores embeddings using FAISS
- Performs similarity search
- Retrieves relevant document information
- Generates answers using Gemini
- Interactive question answering

## 📂 Project Structure

rag-gemini-project/
├── rag_app.py
├── xyz.txt
├── requirements.txt
├── .gitignore
└── README.md

## 🚀 How to Run

### 1. Clone the Repository

git clone https://github.com/naveencholkar/rag-gemini-project.git

### 2. Open the Project

cd rag-gemini-project

### 3. Create Virtual Environment

python -m venv venv

### 4. Activate Virtual Environment

venv\Scripts\activate

### 5. Install Dependencies

pip install -r requirements.txt

### 6. Configure API Key

Create a `.env` file and add:

GOOGLE_API_KEY=your_api_key_here

⚠️ Never upload your actual API key to GitHub.

### 7. Run the Application

python rag_app.py

## 💡 Example

Question:

What is IoT?

Answer:

IoT (Internet of Things) is a technology in which physical devices are connected to the internet and can collect and exchange data.

## 🔍 How FAISS Works

FAISS stores the vector embeddings of document chunks and performs similarity search when the user asks a question. It retrieves the most relevant chunks, which are then provided to Gemini to generate the final answer.

## 🎯 Future Enhancements

- PDF document support
- Multiple document support
- Web-based chatbot
- Document upload functionality
- Source citations
- Chat history

## 📌 Project Status

Completed ✅

## 👨‍💻 Author

Naveen Cholkar

GitHub: https://github.com/naveencholkar

## ⭐ Repository

https://github.com/naveencholkar/rag-gemini-project
