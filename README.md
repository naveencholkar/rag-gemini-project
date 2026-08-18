# RAG Question Answering System using LangChain, Gemini & FAISS

## 📌 About the Project

This project is a Retrieval-Augmented Generation (RAG) based
Question Answering System built using LangChain, Google Gemini,
Gemini Embeddings, and FAISS.

The system loads a document, splits it into smaller chunks,
converts the chunks into embeddings, stores them in a FAISS
vector database, retrieves relevant information, and uses
Gemini to generate an answer.

## 🛠️ Technologies Used

- Python
- LangChain
- Google Gemini
- Gemini Embeddings
- FAISS
- Vector Similarity Search
- VS Code

- ## 🔄 RAG Workflow

Document
↓
Text Loader
↓
Text Chunking
↓
Gemini Embeddings
↓
FAISS Vector Database
↓
User Query
↓
Similarity Search
↓
Top Relevant Chunks
↓
Gemini LLM
↓
Final Answer

## ✨ Features

- Loads text documents
- Splits documents into smaller chunks
- Generates Gemini embeddings
- Stores embeddings using FAISS
- Performs similarity search
- Retrieves relevant document information
- Generates answers using Gemini
- Interactive question answering
- Answers are based on the provided document context

- ## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/naveencholkar/rag-gemini-project.git

cd rag-gemini-project

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

GOOGLE_API_KEY=your_api_key_here

python rag_app.py


⚠️ **Never put your real API key in the README.**

---

## Step 9 — Add example

Add:

```markdown
## 💡 Example

### Question

What is IoT?

### Answer

IoT (Internet of Things) is a technology in which physical
devices are connected to the internet and can collect and
exchange data.

## 👨‍💻 Author

**Naveen Cholkar**

GitHub: https://github.com/naveencholkar
