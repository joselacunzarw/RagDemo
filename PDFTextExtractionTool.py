
import os
import fitz  # PyMuPDF
import re

def sanitize_text(text):
    """Sanitize the text by removing unwanted characters and normalizing spaces."""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove punctuation
    text = text.strip()  # Remove leading and trailing spaces
    return text

def extract_text_chunks(pdf_path, chunk_size):
    """Extract text from a PDF and break it into chunks of specified size."""
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page in doc:
        page_text = page.get_text("text")
        full_text += page_text + " "  # Ensure text from each page is added as a block

    chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]
    
    metadata = []
    current_page = 0
    words_count = 0
    words_in_page = len(doc[current_page].get_text("text").split()) if doc.page_count > 0 else 0

    for i, chunk in enumerate(chunks):
        words = chunk.count(' ') + 1
        words_count += words
        while words_count > words_in_page and current_page < doc.page_count - 1:
            current_page += 1
            words_in_page = len(doc[current_page].get_text("text").split())
            words_count -= words_in_page

        metadata.append({
            'chunk_index': i,
            'page_number': current_page,
            'page': current_page,
            'words_in_chunk': words,
            'file_name': pdf_path,
            'Document url': pdf_path
        })

    doc.close()
    return chunks, metadata

def process_pdf_directory(directory_path, chunk_size):
    """Process a directory of PDF files, extracting text and metadata from each file."""
    all_chunks = []
    all_metadata = []
    for filename in os.listdir(directory_path):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            chunks, metadata = extract_text_chunks(file_path, chunk_size)
            all_chunks.extend(chunks)
            all_metadata.extend(metadata)
    return all_chunks, all_metadata
