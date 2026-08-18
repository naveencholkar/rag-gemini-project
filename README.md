# RAG Question Answering System using LangChain, Gemini & FAISS

## 📌 About the Project

This project is a Retrieval-Augmented Generation (RAG) based Question Answering System built using LangChain, Google Gemini, Gemini Embeddings, and FAISS.

The system loads a document, splits it into smaller chunks, converts the chunks into embeddings, stores them in a FAISS vector database, retrieves relevant information, and uses Gemini to generate an answer.

## 🛠️ Technologies Used

- Python
- LangChain
- Google Gemini
- Gemini Embeddings
- FAISS
- Vector Similarity Search
- VS Code

## 🔄 RAG Workflow

```text
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
