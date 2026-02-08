import os
import re
from pathlib import Path
from typing import List, Dict, Tuple
from dotenv import load_dotenv
import tiktoken
import markdown
from qdrant_client import QdrantClient
from qdrant_client.http import models
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

def extract_module_and_chapter(file_path: str) -> Tuple[str, str]:
    """Extract module and chapter names from file path"""
    path_parts = Path(file_path).parts

    # Find module part
    module = ""
    for part in path_parts:
        if part.startswith('module'):
            module = part
            break

    # Extract chapter name from filename (without extension)
    filename = Path(file_path).stem
    if filename.startswith('chapter'):
        chapter = filename
    else:
        chapter = filename

    return module, chapter

def read_markdown_files(base_path: str = "../physical-ai-book/docs") -> List[Dict]:
    """Read all markdown files from the specified path"""
    documents = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                module, chapter = extract_module_and_chapter(file_path)

                documents.append({
                    'module': module,
                    'chapter': chapter,
                    'text': content,
                    'file_path': file_path
                })

    return documents

def chunk_text(text: str, max_tokens: int = 400) -> List[str]:
    """Split text into chunks based on token count"""
    # Use tiktoken to tokenize
    encoder = tiktoken.encoding_for_model("text-embedding-3-large")

    # Split text into sentences or paragraphs
    paragraphs = re.split(r'\n\s*\n', text)

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        # Encode the potential chunk to count tokens
        potential_chunk = current_chunk + "\n\n" + paragraph if current_chunk else paragraph
        token_count = len(encoder.encode(potential_chunk))

        if token_count <= max_tokens:
            current_chunk = potential_chunk
        else:
            # If the current chunk is not empty, save it and start a new one
            if current_chunk:
                chunks.append(current_chunk.strip())

            # If the paragraph itself is too long, split it into smaller parts
            if len(encoder.encode(paragraph)) > max_tokens:
                sentences = re.split(r'[.!?]+', paragraph)
                temp_chunk = ""

                for sentence in sentences:
                    sentence = sentence.strip()
                    if not sentence:
                        continue

                    potential_sentence_chunk = temp_chunk + " " + sentence if temp_chunk else sentence
                    sentence_token_count = len(encoder.encode(potential_sentence_chunk))

                    if sentence_token_count <= max_tokens:
                        temp_chunk = potential_sentence_chunk
                    else:
                        if temp_chunk:
                            chunks.append(temp_chunk.strip())
                        temp_chunk = sentence

                if temp_chunk:
                    chunks.append(temp_chunk.strip())
            else:
                current_chunk = paragraph

    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def generate_embedding(text: str) -> List[float]:
    """Generate embedding for text using OpenAI's text-embedding-3-large model"""
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-large"
    )
    return response.data[0].embedding

def setup_qdrant_collection(client: QdrantClient, collection_name: str = "physical_ai_rag"):
    """Create Qdrant collection if it doesn't exist"""
    try:
        client.get_collection(collection_name=collection_name)
        print(f"Collection {collection_name} already exists")
    except:
        # Create collection
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=3072, distance=models.Distance.COSINE)  # text-embedding-3-large produces 3072-dimensional vectors
        )
        print(f"Created collection {collection_name}")

def store_in_qdrant(documents: List[Dict], collection_name: str = "physical_ai_rag"):
    """Store documents in Qdrant vector database"""
    # Initialize Qdrant client
    qdrant_client = QdrantClient(
        url=os.getenv("QDRANT_ENDPOINT"),
        api_key=os.getenv("QDRANT_API_KEY")
    )

    # Setup collection
    setup_qdrant_collection(qdrant_client, collection_name)

    # Prepare points for insertion
    points = []
    point_id = 0

    for doc in documents:
        # Chunk the document text
        chunks = chunk_text(doc['text'])

        for chunk in chunks:
            # Generate embedding for the chunk
            embedding = generate_embedding(chunk)

            # Create a point
            point = models.PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "module": doc['module'],
                    "chapter": doc['chapter'],
                    "text": chunk,
                    "file_path": doc['file_path']
                }
            )

            points.append(point)
            point_id += 1

            # Insert in batches of 100 points to manage memory
            if len(points) >= 100:
                qdrant_client.upsert(collection_name=collection_name, points=points)
                print(f"Inserted batch of {len(points)} points")
                points = []  # Reset points list

    # Insert remaining points if any
    if points:
        qdrant_client.upsert(collection_name=collection_name, points=points)
        print(f"Inserted final batch of {len(points)} points")

    print(f"Successfully stored {point_id} chunks in Qdrant collection '{collection_name}'")

def run_ingestion_pipeline():
    """Run the complete ingestion pipeline"""
    print("Starting ingestion pipeline...")

    # Step 1: Read markdown files
    print("Reading markdown files...")
    documents = read_markdown_files()
    print(f"Found {len(documents)} documents")

    # Step 2: Store in Qdrant
    print("Storing documents in Qdrant...")
    store_in_qdrant(documents)

    print("Ingestion pipeline completed!")

if __name__ == "__main__":
    run_ingestion_pipeline()