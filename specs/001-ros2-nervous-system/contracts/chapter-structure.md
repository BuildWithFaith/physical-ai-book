# Chapter Structure Contract

## Contract for ROS 2 Module Chapters

### Required Frontmatter Fields

Each chapter must include the following frontmatter fields:

```yaml
---
id: chapter-[number]-[slug]
title: [Chapter Title]
sidebar_position: [number]
---
```

### Field Specifications

- **id**:
  - Type: string
  - Pattern: `chapter-[number]-[descriptive-slug]`
  - Example: `chapter-1-nervous-system`, `chapter-2-ros-communication`, `chapter-3-digital-brain-to-body`
  - Required: Yes

- **title**:
  - Type: string
  - Purpose: Display title in navigation and page
  - Required: Yes
  - Examples:
    - Chapter 1: "Why Robots Need a Nervous System"
    - Chapter 2: "ROS 2 Communication Primitives"
    - Chapter 3: "From Digital Brain to Physical Body"

- **sidebar_position**:
  - Type: integer
  - Values: 1, 2, or 3 (for chapters 1, 2, 3 respectively)
  - Purpose: Determines order in sidebar navigation
  - Required: Yes

### Content Requirements

Each chapter must contain:
1. H1 heading matching the title in frontmatter
2. Educational content appropriate to the chapter's learning objectives
3. Proper Markdown formatting
4. Forward references to subsequent modules where appropriate
5. Consistent terminology with other chapters

### Validation Rules

1. Every chapter file must begin with valid YAML frontmatter
2. Frontmatter must include all three required fields
3. Sidebar positions must be sequential (1, 2, 3)
4. IDs must be unique across all chapters
5. Content must be in valid Markdown format
6. File extension must be `.md`