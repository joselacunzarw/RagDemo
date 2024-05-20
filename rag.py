import chromadb
import os
from PDFTextExtractionTool import process_pdf_directory

client = chromadb.PersistentClient(path="local_db")
collection = client.get_or_create_collection(name="test")


def query_rag(query):
    results = collection.query(
        query_texts=[query],
        n_results=10
    )
    print (results)
    return results


def process_directory(directory_path, chunk_size):
    """Procesa un directorio de archivos PDF y extrae texto en chunks."""
    if not os.path.exists(directory_path):
        return {'error': 'Directory does not exist'}

    chunks, metadata = process_pdf_directory(directory_path, int(chunk_size))
    for chunk, meta in zip(chunks, metadata):
        collection.add(
            documents=[chunk],
            ids=[str(meta['chunk_index'])],
            metadatas=[{
                'source': 'archivo',
                'page_number': meta['page_number'],
                'words_in_chunk': meta['words_in_chunk'],
                'file_name': meta['file_name'],
                'Document url': meta['Document url']
            }]
        )
    
    return {'message': 'Directorio procesado correctamente', 'chunks': chunks, 'metadata': metadata}