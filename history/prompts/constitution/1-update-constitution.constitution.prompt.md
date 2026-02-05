---
id: 1
title: Update Constitution
stage: constitution
date: 2025-12-26
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: mac
command: sp.constitution
labels: [constitution,spec-driven,ai-book]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
/sp.constitution
Project
Title: AI-Native, Spec-Driven Software Development: From Specifications to Intelligent Systems
Scope:
Author and publish a unified technical book using Docusaurus, deployed to GitHub Pages, accompanied by an embedded Retrieval-Augmented Generation (RAG) chatbot capable of answering questions strictly from the book's content, including user-selected text segments.
Core Principles
Specification Supremacy
All outputs must be derived from explicit, written specifications.
No undocumented assumptions, no emergent behavior.
Accuracy Through Primary Sources
All technical, architectural, and conceptual claims must be traceable to verifiable sources (official docs, peer-reviewed papers, or authoritative standards).
Clarity for a Technical Audience
Content must target readers with a computer science / software engineering background familiar with modern backend, AI, and web systems.
Reproducibility & Determinism
Every architectural decision, code path, and AI behavior must be reproducible from the specs alone.
AI as an Implementer, Not an Author
The AI follows specs; it does not invent scope, features, or interpretations beyond them.
Key Standards
Content & Book Standards
All factual claims must be explicitly verifiable
Citation format: APA
Source mix:
Minimum 50% authoritative technical sources
Peer-reviewed papers
Official platform documentation (OpenAI, FastAPI, Neon, Qdrant, Docusaurus)
Writing clarity:
Technical prose
No marketing language
No speculative claims
Spec-Driven Development Standards
Each chapter must have:
Purpose
Defined inputs
Defined outputs
Explicit non-goals
No chapter may reference functionality not defined in a spec
System Architecture Constraints
Book Platform
Static site generator: Docusaurus
Deployment target: GitHub Pages
Versioned content
Source-controlled markdown only
RAG Chatbot
Architecture:
FastAPI backend
OpenAI Agents / ChatKit SDKs
Neon Serverless Postgres (metadata, sessions, citations)
Qdrant Cloud (Free Tier) for embeddings
Capabilities:
Answer questions strictly from indexed book content
"Selected-text-only" answer mode:
Responses must be grounded only in user-highlighted text
Mandatory citation return for every answer
Forbidden behaviors:
No hallucinated content
No external knowledge injection
No speculative extrapolation beyond indexed text
AI Behavioral Constraints (Mandatory)
The AI must:
Refuse to answer if the answer is not present in the indexed sources
Cite exact document sections used
Surface uncertainty explicitly when information is incomplete
The AI must never:
Fill gaps creatively
Merge external training knowledge with RAG context
Override spec-defined limitations
Verification & Quality Gates
Source verification:
Every non-trivial claim must map to at least one cited source.
Plagiarism tolerance:
0% tolerance — content must be original, paraphrased, and cited.
Fact-checking review:
All chapters and chatbot answers must pass:
Claim-to-source traceability
Architectural correctness
Spec compliance
RAG validation tests:
Query answered correctly from book content
Query refused when content is absent
Selected-text constraint enforced correctly
Deliverables
Docusaurus Book Repository
Complete, structured book
APA citations embedded
GitHub Pages deployment
Spec-Defined RAG System
Backend (FastAPI)
Vector store (Qdrant)
Database (Neon)
OpenAI Agents / ChatKit integration
Specifications
Content specs
RAG behavior specs
Data flow diagrams
Failure & refusal cases
Success Criteria
All content and chatbot answers are spec-traceable
Zero hallucinations under adversarial questioning
Book builds and deploys deterministically
RAG chatbot passes refusal and grounding tests
No violations of constitution principles
```

## Response snapshot

Updated the project constitution at .specify/memory/constitution.md with the specific principles and constraints for the AI-Native, Spec-Driven Software Development project. The new constitution includes:

1. Core Principles:
   - Specification Supremacy
   - AI as an Implementer, Not an Author
   - Clarity for a Technical Audience
   - Reproducibility & Determinism
   - Accuracy Through Primary Sources
   - Zero Hallucination Constraint

2. System Architecture Constraints:
   - Book Platform requirements (Docusaurus, GitHub Pages)
   - RAG Chatbot Architecture (FastAPI, OpenAI Agents, Neon, Qdrant)
   - RAG Capabilities and constraints

3. Development Workflow:
   - Content & Book Standards
   - Spec-Driven Development Standards
   - Verification & Quality Gates

4. Governance section with amendment procedures

The constitution is now properly configured for the project with version 1.0.0.

## Outcome

- ✅ Impact: Created project constitution with all specified principles
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Ready to proceed with spec, plan, and task creation
- 🧠 Reflection: Constitution now properly defines the project's guiding principles and constraints

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin creating feature specifications based on the constitution