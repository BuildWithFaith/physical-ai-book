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