import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
# Load environment variables from .env
load_dotenv()

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "scarlet_letter.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db_Ulysse_is_back")

# Check if the Chroma vector store already exists
# if not os.path.exists(persistent_directory):
if True:
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    # Read the text content from the file
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    # Split the document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n")

    # Create embeddings
    print("\n--- Creating embeddings ---")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )  # Update to a valid embedding model if needed
    print("\n--- Finished creating embeddings ---")

    embedding_vectors = embeddings.embed_documents([doc.page_content for doc in docs])

    # Afficher la dimension d'un embedding
    if embedding_vectors:
        print(f"Dimension d'un embedding : {len(embedding_vectors[0])}")
        # Dimension d'un embedding : 1536
    else:
        print("Aucun embedding généré.")


    # Create the vector store and persist it automatically
    print("\n--- Creating vector store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory,collection_name="CollectionScarlet")
    print("\n--- Finished creating vector store ---")
else:
    print("Vector store already exists. No need to initialize.")
