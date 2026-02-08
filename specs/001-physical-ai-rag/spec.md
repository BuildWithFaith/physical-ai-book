# Feature Specification: Physical AI Book RAG Chatbot

**Feature Branch**: `001-physical-ai-rag`
**Created**: 2026-02-05
**Status**: Draft
**Input**: User description: "Physical AI Book RAG Chatbot"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Chat with Physical AI Book Content (Priority: P1)

As a learner studying Physical AI concepts, I want to interact with a chatbot that can answer questions about the Physical AI book content stored in the physical-ai-book/docs/ directory so that I can get immediate clarification on complex topics without manually searching through modules and chapters.

**Why this priority**: This is the core functionality that provides the primary value of the RAG chatbot - enabling students to get accurate answers to their questions about Physical AI concepts from the book content organized in modules like module-1-ros2, module-2-digital-twin, module-3-ai-robot-brain, and module-4-vision-language-action.

**Independent Test**: Can be fully tested by submitting various questions about Physical AI topics and verifying that the bot responds with accurate information from the book content in the docs/ directory, or indicates when the information is not available.

**Acceptance Scenarios**:

1. **Given** user has opened the chat interface, **When** user submits a question about Physical AI concepts, **Then** the system retrieves relevant content from the docs/ directory and generates an accurate response based on that content
2. **Given** user submits a question not covered in the book content in docs/, **When** the system performs the RAG search, **Then** the system responds with "Not covered in the material"
3. **Given** user is browsing a specific module (e.g., module-1-ros2) or chapter (e.g., chapter-1-nervous-system.md) in the docs/ directory, **When** user submits a question with context, **Then** the system prioritizes relevant results from the same module/chapter

---

### User Story 2 - Access Chat Widget from Any Page (Priority: P2)

As a learner navigating through the Physical AI book website built from the physical-ai-book/docs/ directory, I want to access the chat functionality from any page so that I can get help without leaving my current reading context.

**Why this priority**: This ensures seamless integration with the learning experience, allowing users to get help without interrupting their study flow while browsing content from the docs/ directory.

**Independent Test**: Can be fully tested by visiting different pages on the Docusaurus site generated from docs/ and verifying that the chat widget is accessible and maintains context appropriately.

**Acceptance Scenarios**:

1. **Given** user is viewing any page on the Physical AI book site generated from docs/, **When** user clicks the chat widget, **Then** the chat interface opens and is ready for interaction
2. **Given** user has the chat interface open, **When** user closes the chat, **Then** the main page remains accessible and functional

---

### User Story 3 - Maintain Conversation Context (Priority: P3)

As a learner having a conversation with the Physical AI chatbot, I want to maintain context across multiple exchanges so that I can have meaningful discussions about complex topics from the docs/ directory.

**Why this priority**: This enhances the user experience by enabling more natural conversations, which is essential for deep learning of complex Physical AI concepts found in the modules and chapters.

**Independent Test**: Can be fully tested by conducting multi-turn conversations with the chatbot and verifying that context from the docs/ directory is maintained appropriately.

**Acceptance Scenarios**:

1. **Given** user has an ongoing conversation with the chatbot about content from docs/, **When** user submits follow-up questions, **Then** the system considers the conversation history and book content to provide relevant responses
2. **Given** user's conversation session, **When** session expires, **Then** user receives a clear indication and can start a new conversation

---

### Edge Cases

- What happens when the vector database is temporarily unavailable?
- How does the system handle extremely long or complex queries?
- What occurs when the user submits queries in languages other than English?
- How does the system respond to invalid or nonsensical inputs?
- What happens when the Qdrant search returns no relevant results from the docs/ directory?
- How does the system handle queries about modules that don't exist in the docs/ directory?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a floating chat widget accessible from every page of the Docusaurus site
- **FR-002**: System MUST implement a RAG (Retrieval Augmented Generation) pipeline that retrieves relevant Physical AI book content from Qdrant vector database
- **FR-003**: System MUST generate responses based solely on retrieved content from Qdrant, without external knowledge injection
- **FR-004**: System MUST respond with "Not covered in the material" when requested information is not present in the indexed content in Qdrant
- **FR-005**: System MUST support contextual queries based on current page module/chapter context when available, filtering Qdrant search results accordingly
- **FR-006**: System MUST provide a FastAPI backend with a POST `/chat` endpoint
- **FR-007**: System MUST integrate with Qdrant vector database for content storage and retrieval
- **FR-008**: System MUST use OpenAI embeddings (text-embedding-3-large) for semantic search of content stored in Qdrant
- **FR-009**: System MUST maintain conversation state per session
- **FR-010**: System MUST return source attribution (module + chapter from Qdrant metadata) with each response when possible
- **FR-011**: System MUST process Physical AI book content from physical-ai-book/docs/ directory and store it as vector embeddings in Qdrant
- **FR-012**: System MUST chunk book content into 300-500 token segments when storing in Qdrant
- **FR-013**: System MUST preserve metadata (module, chapter, text) when storing book content in Qdrant

### Key Entities

- **ChatSession**: Represents a user's conversation with the chatbot, including message history and context
- **BookContent**: Represents chunks of Physical AI book content from physical-ai-book/docs/ stored in Qdrant with metadata (module, chapter, text)
- **ChatMessage**: Represents individual user queries and system responses with timestamps and context
- **SearchResult**: Represents relevant book content retrieved from Qdrant based on user query
- **DocumentChunk**: Represents a processed segment of book content (300-500 tokens) stored as vector embeddings in Qdrant with associated metadata

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can submit questions and receive accurate answers from the Physical AI book content within 5 seconds
- **SC-002**: The system correctly identifies when information is not available in the indexed content and responds with "Not covered in the material" 100% of the time
- **SC-003**: At least 90% of user queries about Physical AI concepts receive accurate, relevant responses based on the book content
- **SC-004**: The chat widget is accessible and functional on 100% of pages in the Docusaurus site
- **SC-005**: The system maintains conversation context appropriately across multi-turn interactions about Physical AI concepts
