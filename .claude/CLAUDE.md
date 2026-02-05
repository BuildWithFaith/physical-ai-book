# Physical AI RAG System — Technical Specification

## 1. 📌 Always use Context7 MCP

- Any library, SDK, framework, or API MUST be sourced via Context7.
- Never rely on training-cutoff knowledge.
- Never hallucinate functions, parameters, versions, or behavior.

**Package Manager Specifications:**
- pnpm for JavaScript/TypeScript
- uv for Python

## ENVIRONMENT VARIABLES

Environment configuration is managed via:
- `.env` - Local environment variables (not committed)
- `example.env` - Template with variable names for reference

Variables defined in example.env:
- CONTEXT7_API_KEY
- QDRANT_API_KEY
- QDRANT_ENDPOINT
- OPENAI_API_KEY

## PROJECT SPECIFICATION

You are a senior full-stack AI engineer.

### Goal
Build a Retrieval-Augmented Generation (RAG) chatbot for a technical book built with Docusaurus.
The chatbot must appear on every page and use a FastAPI backend with Qdrant as the vector database.

### System Context
- **Frontend:** Docusaurus (React, TypeScript)
- **Backend:** FastAPI (Python, async)
- **Vector DB:** Qdrant
- **Embeddings Model:** OpenAI text-embedding-3-large
- **Content:** A book on Physical AI
  - **Modules:** 4 modules
  - **Chapters:** Each module has 3 chapters
  - **Chunking:** Chapters to be chunked (300–500 tokens) and should be stored in Qdrant with metadata:
    - `module`
    - `chapter`
    - `text`

### Frontend Requirements

1. **Create a floating ChatWidget** that appears on every page using Docusaurus Layout swizzling.
2. **Lazy Loading:** The widget must be lazy-loaded and not block page rendering.
3. **UI Behavior:**
   - Floating button bottom-right
   - Expands into a modal or side drawer
   - Maintains conversation state per session
4. **Query Sending:**
   - Send user query
   - Send current page module + chapter (if available from URL)
5. **Display:**
   - Show assistant response
   - Optionally show source chapter references.

### Backend Requirements (FastAPI)

1. **Endpoint:** Implement a POST `/chat` endpoint.
2. **Flow:**
   - Receive query + optional module/chapter
   - Generate embedding for the query
   - Perform similarity search in Qdrant (top 3–5 results)
   - Apply metadata filtering when module/chapter is provided
   - Build a strict RAG prompt
   - Call the LLM to generate an answer
3. **Assistant Behavior:**
   - Answer only using retrieved context
   - Say "Not covered in the material" if the answer is not present
4. **Return Values:**
   - Answer text
   - Source metadata (module + chapter)

### Prompt Rules for the LLM

```
"You are a Physical AI tutor.
Answer strictly using the provided context.
If the answer is not present in the context, respond with:
'Not covered in the material.'"
```

### Code Quality Requirements

- Clean, production-ready code
- Async FastAPI endpoints
- Clear folder structure
- Typed request/response models
- No placeholder logic
- No hardcoded secrets
- Comments only where necessary

### Output Expectations

- Provide frontend and backend code separately
- Include key files only (not boilerplate)
- Explain any non-obvious design decisions briefly
- Do not include marketing language or filler text

### Implementation Guidelines

- **Clarification:** Do not ask clarifying questions.
- **Assumptions:** Make reasonable engineering assumptions and proceed.

### Additional Resources

When using OpenAI Agents SDK, reference the openai-agents skill located at `.claude/skills/openai-agents/SKILL.md` for official implementation guidance.

## Active Technologies

- **Backend:** Python 3.11
- **Frontend:** TypeScript/JavaScript
- **Build Tools:** Node.js
- **Frameworks:**
  - FastAPI (backend)
  - Docusaurus (frontend)
  - OpenAI Agents SDK
- **Database:** Qdrant (vector database)