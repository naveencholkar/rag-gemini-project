import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)

# ==========================================================
# 1. LOAD GOOGLE API KEY
# ==========================================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY not found. Check your .env file."
    )

print("Google API key loaded successfully!")


# ==========================================================
# 2. LOAD DOCUMENT
# ==========================================================

loader = TextLoader(
    "xyz.txt",
    encoding="utf-8"
)

raw_documents = loader.load()

print("Document loaded successfully!")


# ==========================================================
# 3. SPLIT DOCUMENT INTO CHUNKS
# ==========================================================

text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

documents = text_splitter.split_documents(
    raw_documents
)

print(
    f"Number of chunks created: {len(documents)}"
)


# ==========================================================
# 4. CREATE GEMINI EMBEDDINGS
# ==========================================================

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=api_key
)

print("Creating embeddings...")


# ==========================================================
# 5. CREATE FAISS VECTOR DATABASE
# ==========================================================

db = FAISS.from_documents(
    documents,
    embeddings
)

print("FAISS vector database created successfully!")


# ==========================================================
# 6. INITIALIZE GEMINI MODEL
# ==========================================================

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)

print("Gemini model initialized successfully!")


# ==========================================================
# 7. INTERACTIVE QUESTION LOOP
# ==========================================================

print("\n========================================")
print("       RAG QUESTION ANSWERING SYSTEM")
print("========================================")
print("Ask questions about your document.")
print("Type 'exit' to close the program.")
print("========================================")


while True:

    # ------------------------------------------------------
    # Get user question
    # ------------------------------------------------------

    query = input("\nEnter your question: ")

    # ------------------------------------------------------
    # Exit program
    # ------------------------------------------------------

    if query.lower().strip() == "exit":
        print("\nRAG application closed.")
        break


    # ------------------------------------------------------
    # 8. SEARCH VECTOR DATABASE
    # ------------------------------------------------------

    results = db.similarity_search(
        query,
        k=3
    )


    # ------------------------------------------------------
    # 9. DISPLAY RETRIEVED CHUNKS
    # ------------------------------------------------------

    print("\n========================================")
    print("TOP RELEVANT DOCUMENT CHUNKS")
    print("========================================")

    for i, doc in enumerate(results, start=1):

        print(f"\n--- Result {i} ---")
        print(doc.page_content)


    # ------------------------------------------------------
    # 10. CREATE CONTEXT
    # ------------------------------------------------------

    context = "\n\n".join(
        doc.page_content
        for doc in results
    )


    # ------------------------------------------------------
    # 11. CREATE RAG PROMPT
    # ------------------------------------------------------

    prompt = f"""
You are an AI assistant that answers questions
using the provided document context.

IMPORTANT RULES:

1. Answer using ONLY the information provided
   in the context.

2. Do not invent information.

3. If the answer cannot be found in the context,
   clearly say:
   "The information is not available in the document."

4. Give a clear and concise answer.

5. If multiple pieces of information are available,
   combine them into a useful answer.

DOCUMENT CONTEXT:
{context}

USER QUESTION:
{query}

ANSWER:
"""


    # ------------------------------------------------------
    # 12. GENERATE RESPONSE USING GEMINI
    # ------------------------------------------------------

    try:

        response = model.invoke(prompt)

        print("\n========================================")
        print("FINAL ANSWER")
        print("========================================")


        # --------------------------------------------------
        # Handle current Gemini response format
        # --------------------------------------------------

        if isinstance(response.content, list):

            for item in response.content:

                if (
                    isinstance(item, dict)
                    and item.get("type") == "text"
                ):

                    print(
                        item.get("text", "")
                    )

        else:

            print(response.content)


    except Exception as e:

        print("\n========================================")
        print("ERROR")
        print("========================================")

        print(f"Something went wrong: {e}")