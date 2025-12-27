# Quickstart Guide: ROS 2 Robotic Nervous System Module

## Prerequisites

- Node.js (version 18 or higher)
- pnpm package manager
- Git

## Setup Instructions

### 1. Install pnpm (if not already installed)
```bash
npm install -g pnpm
```

### 2. Create Docusaurus Project
```bash
pnpm dlx create-docusaurus@latest physical-ai-book classic
cd physical-ai-book
```

### 3. Verify Installation
```bash
pnpm start
```

This will start the development server and open the default Docusaurus site in your browser.

### 4. Install Dependencies
```bash
# Ensure pnpm-lock.yaml is used instead of package-lock.json or yarn.lock
pnpm install
```

## Creating the ROS 2 Module Structure

### 1. Create Module Directory
```bash
mkdir -p docs/module-1-ros2
```

### 2. Create Module Category File
Create `docs/module-1-ros2/_category_.json`:
```json
{
  "label": "Module 1: The Robotic Nervous System (ROS 2)",
  "position": 1,
  "collapsible": true,
  "collapsed": false
}
```

### 3. Create Chapter Files
Create the three required chapter files:
- `docs/module-1-ros2/chapter-1-nervous-system.md`
- `docs/module-1-ros2/chapter-2-ros-communication.md`
- `docs/module-1-ros2/chapter-3-digital-brain-to-body.md`

## Chapter File Structure

Each chapter file must begin with frontmatter:

```markdown
---
id: chapter-1-nervous-system
title: Why Robots Need a Nervous System
sidebar_position: 1
---
```

## Building and Deployment

### Local Development
```bash
pnpm start
```

### Build Static Site
```bash
pnpm build
```

### Deployment to GitHub Pages
1. Configure GitHub Pages in your repository settings
2. Push changes to the main branch
3. The site will be automatically built and deployed

## Important Notes

- All content must be in Markdown format (no .mdx files)
- Use pnpm for all dependency management
- Ensure all content stays within the 2,500-3,500 word range
- Maintain consistent terminology across all chapters
- Include forward references to Module 2 and Module 3 as specified