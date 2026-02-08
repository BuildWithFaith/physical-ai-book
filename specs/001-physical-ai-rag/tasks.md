# Physical AI RAG System — tasks.md

## Project Setup
- [ ] Initialize repository

- [ ] Setup Docusaurus project with pnpm
- [ ] Setup backend project using uv
- [ ] Create `.env`
- [ ] Create `example.env`
- [ ] Add environment variables:
  - [ ] CONTEXT7_API_KEY
  - [ ] QDRANT_API_KEY
  - [ ] QDRANT_ENDPOINT
  - [ ] OPENAI_API_KEY

---

## Backend Setup (FastAPI)
- [ ] Create `backend/` directory
- [ ] Install backend dependencies
- [ ] Initialize FastAPI application
- [ ] Verify server runs locally

Dependencies:
- [ ] fastapi
- [ ] uvicorn
- [ ] openai
- [ ] openai-agents
- [ ] qdrant-client
- [ ] tiktoken
- [ ] python-dotenv

---

## RAG Ingestion Pipeline

### Chapter Conversion
- [ ] Read all module chapter markdown files
- [ ] Extract module name from folder structure
- [ ] Extract chapter name from filename
- [ ] Convert markdown content to plain text

---

### Chunking
- [ ] Implement token-based chunking
- [ ] Chunk size: 300–500 tokens
- [ ] Use tiktoken tokenizer
- [ ] Preserve semantic boundaries

---

### Embedding Generation
- [ ] Implement embedding generator
- [ ] Use `text-embedding-3-large`
- [ ] Validate embedding output

---

### Qdrant Storage
- [ ] Create Qdrant collection
- [ ] Store vectors in Qdrant
- [ ] Store payload metadata:
  - [ ] module
  - [ ] chapter
  - [ ] text
- [ ] Verify stored vectors

---

## Retrieval Pipeline
- [ ] Implement query embedding function
- [ ] Implement Qdrant semantic search
- [ ] Retrieve top 3–5 chunks
- [ ] Build context string from retrieved chunks

---

## Agent Implementation (OpenAI Agents SDK)
- [ ] Create Physical AI tutor agent
- [ ] Add system instructions
- [ ] Ensure agent uses retrieved context only
- [ ] Prevent hallucinated answers
- [ ] Reference `.claude/skills/openai-agents/SKILL.md` when implementing the agent

Agent instruction:
"You are a Physical AI tutor.
Answer strictly using the provided context.
If the answer is not present in the context, respond with:
'Not covered in the material.'"

Implementation guidance:
When using OpenAI Agents SDK, reference the openai-agents skill located at  
`.claude/skills/openai-agents/SKILL.md` for official implementation guidance.

---

## FastAPI Chat API
- [ ] Implement POST `/chat`
- [ ] Accept user query
- [ ] Generate query embedding
- [ ] Retrieve context from Qdrant
- [ ] Send context to agent
- [ ] Return response JSON:
  - [ ] answer
  - [ ] sources

---

## Frontend Chat Widget (Docusaurus)
- [ ] Create ChatWidget component
- [ ] Swizzle Docusaurus Layout
- [ ] Render widget on every page
- [ ] Add floating button UI
- [ ] Add modal or drawer chat window
- [ ] Maintain session conversation state
- [ ] Lazy-load widget
- [ ] Connect widget to `/chat` endpoint
- [ ] Render assistant responses
- [ ] Display source references

---

## Testing
- [ ] Run ingestion pipeline
- [ ] Verify vectors exist in Qdrant
- [ ] Test semantic retrieval
- [ ] Test `/chat` endpoint
- [ ] Test agent responses
- [ ] Test frontend chat widget
- [ ] End-to-end RAG test

---

## Production Readiness
- [ ] Async FastAPI endpoints
- [ ] Typed request/response models
- [ ] Clean folder structure
- [ ] No placeholder logic
- [ ] No hardcoded secrets
- [ ] Minimal comments