<!-- SYNC IMPACT REPORT
Version change: 1.0.0 -> 2.0.0
Modified principles: Complete overhaul of constitution for Physical AI RAG Chatbot Project
Added sections: Physical AI Domain Focus, Strict RAG Implementation, Real-time Chat Interface, Technical Documentation Standards
Removed sections: Previous generic AI development principles
Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md
Follow-up TODOs: None
-->
# Physical AI Book RAG Chatbot Development Constitution

## Core Principles

### Physical AI Domain Specialization
All development must prioritize accuracy and fidelity to Physical AI concepts, theories, and applications. Content must reflect rigorous scientific and engineering principles specific to physical AI systems including robotics, embodied intelligence, sensorimotor learning, and physics-aware machine learning.

### Strict RAG Implementation
The system must adhere to strict retrieval-augmented generation principles where answers are generated solely from retrieved context. If the required information is not present in the retrieved documents, the system must respond with "Not covered in the material." No external knowledge injection is permitted.

### Real-time Chat Interface Excellence
The frontend chat widget must provide seamless, responsive user experience integrated into the Docusaurus site. The interface must support contextual conversations, maintain session state, and properly attribute sources from the Physical AI book content.

### Technical Stack Compliance
All implementations must strictly follow the designated technology stack: FastAPI for backend services, Docusaurus for frontend documentation site, Qdrant for vector storage, OpenAI Agents SDK full stack framework for building AI Agents we will use it to make Chat Agent that will reply to the user, and OpenAI embeddings for semantic search. Deviations require explicit approval and justification.

### Content Fidelity Assurance
All book content must be accurately represented in the vector database with proper metadata (module, chapter, text). Chunking must preserve semantic coherence while maintaining the educational integrity of Physical AI concepts.

### Quality & Verification Standards
Every feature must undergo comprehensive testing including RAG accuracy validation, UI responsiveness checks, and content retrieval precision. All implementations must meet production-ready standards with proper error handling and performance optimization.

## System Architecture Constraints

### Frontend Architecture
Docusaurus-based static site with React/TypeScript components. Chat widget must be implemented as a floating element with lazy loading to prevent blocking page render. Widget must maintain conversation state per session and integrate seamlessly with the existing Docusaurus layout.

### Backend Architecture
FastAPI asynchronous endpoints for handling chat requests. Service must accept queries with optional module/chapter context, perform vector similarity search in Qdrant, construct RAG prompts, and return responses with source attribution. Error handling and rate limiting must be implemented.

### Vector Database Integration
Qdrant vector database must store book content as semantically-meaningful chunks (300-500 tokens) with associated metadata. Search functionality must support both general queries and filtered searches based on module/chapter context when provided.

### Embedding Strategy
OpenAI text-embedding-3-large model must be used for generating vector embeddings. The system must properly handle embedding generation for both document indexing and query processing while maintaining consistency in the embedding space.

## Development Workflow

### Implementation Standards
All code must be typed, documented, and follow clean architecture principles. Type safety must be enforced with TypeScript on frontend and Python type hints on backend. Error handling must be comprehensive and logging must facilitate debugging without exposing sensitive information.

### Testing & Validation
Unit tests for backend services, integration tests for RAG pipeline, and end-to-end tests for chat interface. Validation must include content accuracy, response time performance, and proper handling of edge cases like empty queries or unavailable content.

### Security & Privacy
No user data should be stored beyond session requirements. All API calls must be secured with proper authentication. Environment variables must be properly managed and not committed to version control.

### Performance Optimization
Frontend assets must be optimized for fast loading. Backend endpoints must be efficient with proper caching where appropriate. Vector searches must be optimized for response time while maintaining accuracy.

## Governance

This constitution governs all development activities for the Physical AI RAG chatbot project. All contributions must comply with these principles. Changes to the constitution require explicit approval and documentation of the rationale. All pull requests must be reviewed for compliance with these principles before merging.

The constitution ensures that the final product serves as an authoritative resource for Physical AI education while providing reliable, contextually-aware assistance to learners.

**Version**: 2.0.0 | **Ratified**: 2026-02-05 | **Last Amended**: 2026-02-05