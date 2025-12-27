<!-- SYNC IMPACT REPORT
Version change: N/A -> 1.0.0
Modified principles: N/A (new constitution)
Added sections: All sections added based on project requirements
Removed sections: N/A
Templates requiring updates: N/A
Follow-up TODOs: None
-->
# AI-Native, Spec-Driven Software Development Constitution

## Core Principles

### Specification Supremacy
All outputs must be derived from explicit, written specifications. No undocumented assumptions, no emergent behavior. Accuracy Through Primary Sources: All technical, architectural, and conceptual claims must be traceable to verifiable sources (official docs, peer-reviewed papers, or authoritative standards).

### AI as an Implementer, Not an Author
The AI follows specs; it does not invent scope, features, or interpretations beyond them. This ensures reproducibility and deterministic behavior in all AI-assisted development processes.

### Clarity for a Technical Audience
Content must target readers with a computer science / software engineering background familiar with modern backend, AI, and web systems. All communication must be precise and technically accurate.

### Reproducibility & Determinism
Every architectural decision, code path, and AI behavior must be reproducible from the specs alone. This ensures that all development processes can be consistently replicated and verified.

### Accuracy Through Primary Sources
All technical, architectural, and conceptual claims must be traceable to verifiable sources (official docs, peer-reviewed papers, or authoritative standards). Citation format: APA. Minimum 50% authoritative technical sources including peer-reviewed papers and official platform documentation.

### Zero Hallucination Constraint
AI behavioral constraint: The AI must refuse to answer if the answer is not present in the indexed sources, cite exact document sections used, and surface uncertainty explicitly when information is incomplete. The AI must never fill gaps creatively, merge external training knowledge with RAG context, or override spec-defined limitations.

## System Architecture Constraints

### Book Platform
Static site generator: Docusaurus. Deployment target: GitHub Pages. Versioned content. Source-controlled markdown only.

### RAG Chatbot Architecture
Backend: FastAPI. OpenAI Agents / ChatKit SDKs. Neon Serverless Postgres (metadata, sessions, citations). Qdrant Cloud (Free Tier) for embeddings.

### RAG Capabilities
Answer questions strictly from indexed book content. "Selected-text-only" answer mode: Responses must be grounded only in user-highlighted text. Mandatory citation return for every answer. Forbidden behaviors: No hallucinated content, No external knowledge injection, No speculative extrapolation beyond indexed text.

## Development Workflow

### Content & Book Standards
All factual claims must be explicitly verifiable. Source mix: Minimum 50% authoritative technical sources, Peer-reviewed papers, Official platform documentation (OpenAI, FastAPI, Neon, Qdrant, Docusaurus). Writing clarity: Technical prose, No marketing language, No speculative claims.

### Spec-Driven Development Standards
Each chapter must have: Purpose, Defined inputs, Defined outputs, Explicit non-goals. No chapter may reference functionality not defined in a spec.

### System Architecture Constraints
All architectural decisions must align with the specified technology stack and deployment targets. Every component must be spec-compliant and verifiable against the defined requirements.

### Verification & Quality Gates
Source verification: Every non-trivial claim must map to at least one cited source. Plagiarism tolerance: 0% tolerance — content must be original, paraphrased, and cited. Fact-checking review: All chapters and chatbot answers must pass: Claim-to-source traceability, Architectural correctness, Spec compliance. RAG validation tests: Query answered correctly from book content, Query refused when content is absent, Selected-text constraint enforced correctly.

## Governance

The constitution supersedes all other practices and development guidelines. All development must verify compliance with these principles. Amendments require documentation, approval, and migration plan if applicable. All PRs/reviews must verify constitution compliance. Complexity must be justified against these principles. Use specification documents for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2025-12-26 | **Last Amended**: 2025-12-26