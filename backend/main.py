from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
import asyncio
from retrieval import query_rag_system

# Load environment variables
load_dotenv()

app = FastAPI(title="Physical AI RAG System", version="1.0.0")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    query: str
    top_k: Optional[int] = 5

# Response model
class Source(BaseModel):
    module: str
    chapter: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]

@app.get("/")
async def root():
    return {"message": "Physical AI RAG System Backend"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Chat endpoint that processes user queries using RAG"""
    try:
        # Process the query through the RAG system
        result = await asyncio.get_event_loop().run_in_executor(
            None, query_rag_system, request.query, request.top_k
        )

        return ChatResponse(
            answer=result["answer"],
            sources=result["sources"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)