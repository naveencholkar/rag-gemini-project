# 🤖 RAG Question Answering System using LangChain, Google Gemini & FAISS

## 📌 Project Overview

This project is a **Retrieval-Augmented Generation (RAG) based Question Answering System** developed using Python, LangChain, Google Gemini, Gemini Embeddings, and FAISS.

The system allows users to ask questions about information contained in a document. Instead of sending the question directly to the Large Language Model (LLM), the system first searches the document for the most relevant information and then provides that information to Gemini to generate the final answer.

This approach helps the system generate answers based on the provided document context.

---

## 🎯 Objective

The main objective of this project is to build a simple and practical RAG pipeline that can:

- Load a document
- Split the document into smaller chunks
- Convert document chunks into vector embeddings
- Store embeddings in a FAISS vector database
- Search for relevant information using similarity search
- Pass the retrieved information to Google Gemini
- Generate a final answer based on the retrieved document context

---

## 🧠 What is RAG?

**RAG stands for Retrieval-Augmented Generation.**

RAG combines two major processes:

1. **Retrieval** – Find the most relevant information from the provided documents.
2. **Generation** – Use an LLM such as Google Gemini to generate a natural-language answer using the retrieved information.

### Basic RAG Process

```text
User Question
      ↓
Question Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks
      ↓
Context + User Question
      ↓
Google Gemini
      ↓
Generated Answer

🔄 Complete Project Workflow
                 ┌─────────────────┐
                 │    xyz.txt      │
                 │    Document     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │   Text Loader   │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Text Chunking   │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Gemini          │
                 │ Embeddings      │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ FAISS Vector    │
                 │ Database        │
                 └────────┬────────┘
                          │
                          │
                    User Question
                          │
                          ↓
                 ┌─────────────────┐
                 │ Similarity      │
                 │ Search          │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Top Relevant    │
                 │ Chunks          │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Prompt with     │
                 │ Retrieved Data  │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Google Gemini   │
                 │ LLM             │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Final Answer    │
                 └─────────────────┘
🛠️ Technologies Used
| Technology           | Purpose                                   |
| -------------------- | ----------------------------------------- |
| Python               | Main programming language                 |
| LangChain            | RAG application framework                 |
| Google Gemini        | Large Language Model                      |
| Gemini Embeddings    | Converts text into vector representations |
| FAISS                | Vector database and similarity search     |
| Google Generative AI | Access to Gemini services                 |
| VS Code              | Development environment                   |
| Git & GitHub         | Version control and project hosting       |

✨ Features

📄 Loads text documents
✂️ Splits documents into smaller chunks
🧠 Generates vector embeddings using Gemini
🗄️ Stores embeddings using FAISS
🔎 Performs similarity search
📚 Retrieves the most relevant document chunks
🤖 Generates answers using Google Gemini
💬 Interactive question-answering system
🔐 Uses environment variables for API key protection
⚡ Fast vector similarity search using FAISS

📂 Project Structure
rag-gemini-project/
│
├── rag_app.py
│   └── Main RAG application
│
├── xyz.txt
│   └── Source document used by the RAG system
│
├── requirements.txt
│   └── Python dependencies
│
├── .gitignore
│   └── Prevents sensitive/unnecessary files from being uploaded
│
├── .env
│   └── Google Gemini API key
│
└── README.md
    └── Project documentation

🚀 Installation and Setup
1. Clone the Repository
git clone https://github.com/naveencholkar/rag-gemini-project.git
2. Open the Project
cd rag-gemini-project
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

For Windows:

venv\Scripts\activate
5. Install Required Packages
pip install -r requirements.txt
🔑 Google Gemini API Key Setup

Create a .env file in the project directory.

Add:

GOOGLE_API_KEY=your_api_key_here

Replace your_api_key_here with your own Google Gemini API key.

⚠️ Security

Never upload your real API key to GitHub.

The .gitignore file should contain:

.env
venv/
__pycache__/
*.pyc
▶️ Run the Application

After activating the virtual environment, run:

python rag_app.py

The application will display:

========================================
       RAG QUESTION ANSWERING SYSTEM
========================================


Ask questions about your document.
Type 'exit' to close the program.

You can then enter your question.

💡 Example
Question
What is IoT?
Retrieved Information

The system retrieves the relevant document chunks related to IoT.

Generated Answer
IoT (Internet of Things) is a technology in which physical
devices are connected to the internet and can collect and
exchange data.
🧪 Example Questions

You can test the application with questions such as:

What is IoT?
What are the applications of IoT?
What communication technologies are used in IoT?
What devices can be used in a smart home?
Why is IoT useful?
🔍 RAG Retrieval Example

For a question such as:

What are the applications of IoT?

The system performs:

Question
   ↓
Embedding
   ↓
FAISS Search
   ↓
Relevant Document Chunks
   ↓
Gemini
   ↓
Final Answer

This demonstrates the complete Retrieval-Augmented Generation workflow.

📊 Advantages of the Project
Reduces dependency on general model knowledge
Provides answers based on the supplied document
Makes document-based question answering easier
Uses semantic similarity instead of simple keyword matching
Can be extended to PDFs and multiple documents
Can be integrated into a web-based chatbot
Provides a practical implementation of modern Generative AI concepts
🔮 Future Enhancements

The current project can be extended with:

📄 PDF document support
📚 Multiple document upload
🌐 Web-based user interface
💬 Chatbot-style conversation
📑 Document source citations
🗂️ Multiple document collections
🔎 Improved semantic search
🧠 Conversation memory
☁️ Cloud deployment
📱 Responsive web interface
🎓 Learning Outcomes

Through this project, the following concepts were implemented:

Retrieval-Augmented Generation (RAG)
Large Language Models (LLMs)
Vector embeddings
Vector databases
Similarity search
LangChain
Google Gemini API
FAISS
Document chunking
Prompt construction
Environment variable management
Git and GitHub
📸 Sample Output
========================================
       RAG QUESTION ANSWERING SYSTEM
========================================


Enter your question: What is IoT?


========================================
TOP RELEVANT DOCUMENT CHUNKS
========================================


--- Result 1 ---
Internet of Things


Internet of Things, commonly called IoT, is a technology
in which physical devices are connected to the internet
and can collect and exchange data.


--- Result 2 ---
IoT communication technologies include Wi-Fi, Bluetooth,
Zigbee, LoRaWAN and cellular networks.


========================================
FINAL ANSWER
========================================


IoT (Internet of Things) is a technology in which physical
devices are connected to the internet and can collect and
exchange data.
📌 Project Status

Status: Completed ✅

The current version successfully implements:

Document loading ✅
Document chunking ✅
Gemini embeddings ✅
FAISS vector database ✅
Similarity search ✅
Relevant document retrieval ✅
Gemini response generation ✅
Interactive question answering ✅
👨‍💻 Author
Naveen Cholkar

GitHub:
https://github.com/naveencholkar

⭐ Project Repository

GitHub Repository:

https://github.com/naveencholkar/rag-gemini-project
