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
    collection = client.get_collection(collection_names[1])  # Par exemple, la première collection
    print(f"Utilisation de la collection : {collection.name}")
    num_entries = collection.count()  # Nombre total d'entrées/vecteurs
    print(f"Nombre d'entrées dans la collection : {num_entries}") # 489
    
    # Accéder aux dimensions d'un vecteur (par exemple, le premier vecteur)
    if num_entries > 0:
        results = collection.get(limit=3, include=["embeddings", "documents", "metadatas"])
        first_id = results['ids'][0]
        first_embedding = results['embeddings'][0]
        first_document = results['documents'][0]
        first_metadata = results['metadatas'][0]

        # last_id = results['ids'][num_entries-1]
        last_id = results['ids'][2]
        
        # Afficher les informations
        print(f"ID du premier vecteur : {first_id}") # 00e82f9b-d3d7-4d1a-953d-79bc9720b966
        print(f"Dimensions du vecteur : {len(first_embedding)}") # 1536
        # print(f"Vecteur : {first_embedding}") # see file nombreVecteur.py
        print(f"Document associé : {first_document}") #  Cambridge: Electrotyped and Printed by Welch, Bigelow, & Co.
        print(f"Métadonnées associées : {first_metadata}") # {'source': 'C:\\Users\\franc\\OneDrive\\Documents\\vsc\\langchain-crash-course\\4_rag\\books\\scarlet_letter.txt'} 
    else:
        print("La collection est vide.")
else:
    print("Aucune collection disponible. Veuillez en créer une.")

