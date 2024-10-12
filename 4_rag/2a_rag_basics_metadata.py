import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
# Load environment variables from .env
load_dotenv()

# Define the maximum batch size
MAX_BATCH_SIZE = 5461

# Define the directory containing the text files and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
books_dir = os.path.join(current_dir, "books")
db_dir = os.path.join(current_dir, "db")
persistent_directory = os.path.join(db_dir, "chroma_db_with_metadata")

print(f"Books directory: {books_dir}")
print(f"Persistent directory: {persistent_directory}")

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensure the books directory exists
    if not os.path.exists(books_dir):
        raise FileNotFoundError(
            f"The directory {books_dir} does not exist. Please check the path."
        )

    # List all text files in the directory
    book_files = [f for f in os.listdir(books_dir) if f.endswith(".txt")]

    # Read the text content from each file and store it with metadata
    documents = []
    print (f"len(book_files) : {len(book_files)} ")
    for book_file in book_files:
        file_path = os.path.join(books_dir, book_file)
        loader = TextLoader(file_path, encoding="utf-8")
        book_docs = loader.load()
        print (f"book_file {book_file} len(book_docs) {len(book_docs)} ")
        for doc in book_docs:
            # Add metadata to each document indicating its source
            doc.metadata = {"source": book_file}
            documents.append(doc)

    # Split the documents into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")

    # Create embeddings
    print("\n--- Creating embeddings ---")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )  # Update to a valid embedding model if needed
    print("\n--- Finished creating embeddings ---")

    # Create the vector store and persist it
    print("\n--- Creating and persisting vector store ---")

    # code d'origine qui ne fonctionnait pas / limitation à des batchs de 5461 documents
    # db = Chroma.from_documents(
    #     docs, embeddings, persist_directory=persistent_directory)

    for i in range(0, len(docs), MAX_BATCH_SIZE):
            batch_docs = docs[i:i + MAX_BATCH_SIZE]
            print(f"Processing batch {i // MAX_BATCH_SIZE + 1} with {len(batch_docs)} documents.")
            db = Chroma.from_documents(
                batch_docs, embeddings, persist_directory=persistent_directory
            )
            # Persist the database after each batch
            db.persist()

    print("\n--- Finished creating and persisting vector store ---")
else:
    print("Vector store already exists. No need to initialize.")

# Processing batch 1 with 5461 documents.
# Processing batch 2 with 5461 documents.
# Processing batch 3 with 2545 documents.
