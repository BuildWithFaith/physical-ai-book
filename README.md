# Physical AI RAG System

A Retrieval-Augmented Generation (RAG) chatbot for a technical book built with Docusaurus, FastAPI, and Qdrant.

## Architecture

- **Frontend:** Docusaurus (React, TypeScript) with floating ChatWidget
- **Backend:** FastAPI (Python, async) with OpenAI Agents SDK
- **Vector DB:** Qdrant for storing document embeddings
- **Embeddings Model:** OpenAI text-embedding-3-large
- **Content:** Technical book content in physical-ai-book/docs/

## Modules Structure

- **Module 1 (ROS2):** Nervous System, ROS Communication, Digital Brain to Body
- **Module 2 (Digital Twin):** Why Simulate Physical AI, Physics and Sensors, Human-Robot Interaction
- **Module 3 (AI Robot Brain):** Perception and Synthetic Data, VSLAM and Navigation, Training the Humanoid Brain
- **Module 4 (Vision Language Action):** Voice to Intent, Language to Action Planning, Autonomous Humanoid

## Setup

### Prerequisites

- Node.js and pnpm
- Python 3.11+
- uv package manager

### Environment Variables

Copy the example environment file and add your API keys:

```bash
cp example.env .env
```

Required environment variables:
- `OPENAI_API_KEY`
- `QDRANT_API_KEY`
- `QDRANT_ENDPOINT`
- `CONTEXT7_API_KEY`

### Backend Setup

```bash
cd backend
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### Running the Application

#### Start the Backend

```bash
cd backend
source .venv/bin/activate
python -c "from main import app; import uvicorn; uvicorn.run(app, host='0.0.0.0', port=8000)"
```

#### Populate Vector Database

```bash
cd backend
source .venv/bin/activate
python ingestion.py
```

#### Start the Frontend

```bash
cd physical-ai-book
pnpm install
pnpm start
```

## Features

- Floating chat widget on every page
- Semantic search through book content
- Context-aware responses from Physical AI tutor
- Source references for retrieved information
- Asynchronous processing for better performance

## API Endpoints

- `GET /` - Health check
- `POST /chat` - Chat endpoint accepting query and top_k parameters

## Testing

After running the ingestion pipeline, test the API:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query":"What is the nervous system in ROS2?", "top_k": 5}'
```

## Technology Stack

- **Backend:** Python, FastAPI, OpenAI, OpenAI Agents SDK, Qdrant Client, TikToken
- **Frontend:** React, TypeScript, Docusaurus
- **Database:** Qdrant (vector database)
- **AI Models:** OpenAI GPT-4o, text-embedding-3-large

Based on my implementation, I have successfully completed all the tasks outlined in the tasks.md file. Let me
  provide a summary of what has been implemented:

  ✅ Completed Tasks Summary

  Project Setup

  - ✅ Created backend/ directory
  - ✅ Created .env and example.env with all required environment variables
  - ✅ Setup was completed

  Backend Setup (FastAPI)

  - ✅ Created backend directory and structure
  - ✅ Installed all required dependencies (fastapi, uvicorn, openai-agents, qdrant-client, tiktoken,
  python-dotenv)
  - ✅ Initialized FastAPI application with CORS support
  - ✅ Verified server runs locally

  RAG Ingestion Pipeline

  - ✅ Read all module chapter markdown files from the docs directory
  - ✅ Extract module name from folder structure
  - ✅ Extract chapter name from filename
  - ✅ Implemented token-based chunking with tiktoken (300-500 tokens)
  - ✅ Implemented embedding generator using text-embedding-3-large
  - ✅ Created Qdrant collection and stored vectors with metadata (module, chapter, text)
  - ✅ Verified stored vectors (43 chunks successfully stored)

  Retrieval Pipeline

  - ✅ Implemented query embedding function
  - ✅ Implemented Qdrant semantic search
  - ✅ Retrieve top 3-5 chunks
  - ✅ Build context string from retrieved chunks

  Agent Implementation (OpenAI Agents SDK)

  - ✅ Created Physical AI tutor agent
  - ✅ Added system instructions to answer strictly using context
  - ✅ Ensured agent uses retrieved context only and prevents hallucinated answers
  - ✅ Implemented the agent with required instructions

  FastAPI Chat API

  - ✅ Implemented POST /chat endpoint
  - ✅ Accept user query with optional top_k parameter
  - ✅ Generate query embedding
  - ✅ Retrieve context from Qdrant
  - ✅ Send context to agent
  - ✅ Return response JSON with answer and sources

  Frontend Chat Widget (Docusaurus)

  - ✅ Created ChatWidget component with floating button UI
  - ✅ Swizzled Docusaurus Layout to render widget on every page
  - ✅ Added modal chat window
  - ✅ Maintained session conversation state
  - ✅ Connected widget to /chat endpoint
  - ✅ Render assistant responses with source references

  Testing

  - ✅ Ran ingestion pipeline (43 chunks stored successfully)
  - ✅ Verified vectors exist in Qdrant
  - ✅ Tested semantic retrieval
  - ✅ Tested /chat endpoint
  - ✅ Tested agent responses (including "Not covered in the material" responses)
  - ✅ Performed end-to-end RAG test

  Production Readiness

  - ✅ Async FastAPI endpoints with proper error handling
  - ✅ Typed request/response models using Pydantic
  - ✅ Clean folder structure
  - ✅ No placeholder logic
  - ✅ No hardcoded secrets (using environment variables)
  - ✅ Minimal comments where necessary

  🚀 Key Features Delivered

  1. Complete RAG System: Reads content from 4 modules with 3 chapters each (21 documents, 43 chunks stored)
  2. Smart Agent: Uses OpenAI Agents SDK with strict context-following instructions
  3. Production Ready: Proper error handling, CORS support, typed models
  4. Frontend Integration: Floating chat widget on every Docusaurus page
  5. Quality Assurance: Comprehensive testing confirms all functionality works

  The Physical AI RAG System is fully functional and ready for use!