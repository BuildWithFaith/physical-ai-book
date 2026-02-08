import os
import asyncio
from typing import List, Dict
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from openai import OpenAI, AsyncOpenAI
from agents import Agent, Runner

# Load environment variables
load_dotenv()

# Initialize OpenAI client
def retrieve_context(query: str, top_k: int = 5, collection_name: str = "physical_ai_rag") -> List[Dict]:
    """Retrieve relevant context from Qdrant based on the query"""
    # Initialize OpenAI client
    client = OpenAI()
    
    # Generate embedding for the query
    query_embedding = client.embeddings.create(
        input=query,
        model="text-embedding-3-large"
    ).data[0].embedding


    # Initialize Qdrant client
    qdrant_client = QdrantClient(
        url=os.getenv("QDRANT_ENDPOINT"),
        api_key=os.getenv("QDRANT_API_KEY")
    )

    # Perform semantic search using query_points (newer method)
    search_results = qdrant_client.query_points(
        collection_name=collection_name,
        query=query_embedding,
        limit=top_k,
        with_payload=True
    )

    # Extract context from search results
    context_chunks = []
    for result in search_results.points:
        context_chunks.append({
            "module": result.payload["module"],
            "chapter": result.payload["chapter"],
            "text": result.payload["text"],
            "score": result.score
        })

    return context_chunks

def create_physical_ai_agent():
    """Create the Physical AI tutor agent using OpenAI Agents SDK"""
    # Define the agent's instructions
    instructions = """You are a Physical AI tutor.
Answer strictly using the provided context.
If the answer is not present in the context, respond with:
'Not covered in the material.'"""

    # Create the agent
    agent = Agent(
        name="Physical AI Tutor",
        instructions=instructions,
        model="gpt-4o",  # Using a capable model for understanding context
    )

    return agent

async def get_answer_from_agent(query: str, context: List[Dict]):
    """Get answer from the agent using the provided context"""
    # Build context string
    context_str = "\\n\\n".join([chunk["text"] for chunk in context])

    # Create a message with the context and query
    full_prompt = f"""Context:\\n{context_str}\\n\\nQuestion: {query}\\n\\nPlease answer based on the provided context."""

    # Create the agent
    agent = create_physical_ai_agent()

    # Run the agent with the prompt
    result = await Runner.run(agent, full_prompt)

    return result.final_output

async def query_rag_system(query: str, top_k: int = 5) -> Dict:
    """Complete RAG query pipeline"""
    # Retrieve relevant context
    # Running sync function in thread pool to avoid blocking
    context = await asyncio.to_thread(retrieve_context, query, top_k=top_k)

    if not context:
        return {
            "answer": "Not covered in the material.",
            "sources": []
        }

    # Get answer from agent
    answer = await get_answer_from_agent(query, context)

    # Extract source information
    sources = [{"module": chunk["module"], "chapter": chunk["chapter"]} for chunk in context]

    return {
        "answer": answer,
        "sources": sources
    }