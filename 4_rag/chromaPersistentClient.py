import chromadb
import os
from chromadb.config import Settings

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db_Ulysse_is_back")

client = chromadb.PersistentClient(path=persistent_directory)

collections = client.list_collections()
collection_names = [col.name for col in collections]
print("Available collections :", collection_names)

if collection_names:
    collection = client.get_collection(collection_names[0])  # Par exemple, la première collection
    print(f"Utilisation de la collection : {collection.name}")
else:
    print("Aucune collection disponible. Veuillez en créer une.")