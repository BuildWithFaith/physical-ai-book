# Implementation Plan: Modules 2-4 Docusaurus Structure
## Book: Physical AI & Humanoid Robotics

### Technical Context

**Feature Overview**: Implementation of Modules 2-4 for the Physical AI & Humanoid Robotics book, following the existing Docusaurus structure established in Module 1.

**Target Architecture**: Docusaurus documentation site with modular organization following the pattern established in Module 1.

**Current State**:
- Repository contains existing Docusaurus site with Module 1 (ROS 2) already implemented
- Module 1 directory exists at `docs/module-1-ros2/` with proper structure
- Docusaurus configuration is already set up
- Sidebars are configured to show Module 1

**Implementation Requirements**:
- Create 3 new module directories in `docs/`
- Each module must have `_category_.json` for sidebar registration
- Each module contains exactly 3 chapters as `.md` files
- All chapters must have required frontmatter
- No MDX usage allowed (only `.md` files)
- Proper positioning in navigation hierarchy

### Constitution Check

Based on `.specify/memory/constitution.md` principles:
- ✅ All content will be in `.md` format for Docusaurus v3.x
- ✅ Following existing architectural patterns from Module 1
- ✅ Maintaining conceptual + architectural focus (no implementation tutorials)
- ✅ Using forward references only (no backward dependencies)
- ✅ Small, testable changes with precise code references

### Gates

**Gate 1: Architecture Review** - All directory structures created and validated
**Gate 2: Content Contract** - All chapter files have proper frontmatter and positioning
**Gate 3: Integration Test** - Sidebar renders correctly with new modules
**Gate 4: Validation Gate** - All requirements satisfied (no MDX, proper ordering, etc.)

---

## Phase 0: Research & Analysis

### Research Tasks

1. **Analyze existing Module 1 structure**
   - Decision: Follow the same pattern for Modules 2-4
   - Rationale: Consistency with existing architecture
   - Alternatives considered: Different directory structures (rejected for consistency)

2. **Understand Docusaurus sidebar configuration**
   - Decision: Use `_category_.json` files for navigation
   - Rationale: Standard Docusaurus pattern
   - Alternatives considered: Other navigation methods (not applicable)

3. **Confirm content requirements from spec**
   - Decision: Each module gets exactly 3 chapters as specified
   - Rationale: Alignment with learning objectives
   - Alternatives considered: Different chapter counts (not applicable)

---

## Phase 1: Directory Structure & Scaffolding

### Step 1: Create Module Directories

Create the following directory structure in `physical-ai-book/docs/`:
```
docs/
├── module-1-ros2/          (existing)
├── module-2-digital-twin/  (new)
├── module-3-ai-robot-brain/ (new)
├── module-4-vision-language-action/ (new)
```

### Step 2: Create Category Files

Create `_category_.json` for each new module:

**Module 2** - `physical-ai-book/docs/module-2-digital-twin/_category_.json`:
```json
{
  "label": "Module 2: The Digital Twin",
  "position": 2,
  "collapsible": true,
  "collapsed": false
}
```

**Module 3** - `physical-ai-book/docs/module-3-ai-robot-brain/_category_.json`:
```json
{
  "label": "Module 3: The AI-Robot Brain",
  "position": 3,
  "collapsible": true,
  "collapsed": false
}
```

**Module 4** - `physical-ai-book/docs/module-4-vision-language-action/_category_.json`:
```json
{
  "label": "Module 4: Vision-Language-Action",
  "position": 4,
  "collapsible": true,
  "collapsed": false
}
```

### Step 3: Create Chapter Files

Create exactly 3 `.md` chapters for each module:

**Module 2 chapters**:
- `chapter-1-why-simulate-physical-ai.md`
- `chapter-2-physics-and-sensors.md`
- `chapter-3-human-robot-interaction.md`

**Module 3 chapters**:
- `chapter-1-perception-and-synthetic-data.md`
- `chapter-2-vslam-and-navigation.md`
- `chapter-3-training-the-humanoid-brain.md`

**Module 4 chapters**:
- `chapter-1-voice-to-intent.md`
- `chapter-2-language-to-action-planning.md`
- `chapter-3-the-autonomous-humanoid.md`

### Step 4: Apply Required Frontmatter

Every chapter file must start with:
```
---
id: <unique-id>
title: <chapter title>
sidebar_position: <number>
---
```

Where:
- `id` is unique across all documents
- `title` matches the chapter's purpose
- `sidebar_position` is 1, 2, or 3 for the chapter order within each module

---

## Phase 2: Implementation Tasks

### Task 1: Directory Creation
- [ ] Create `module-2-digital-twin/` directory
- [ ] Create `module-3-ai-robot-brain/` directory
- [ ] Create `module-4-vision-language-action/` directory

### Task 2: Category File Creation
- [ ] Create `_category_.json` for Module 2
- [ ] Create `_category_.json` for Module 3
- [ ] Create `_category_.json` for Module 4

### Task 3: Chapter File Creation
- [ ] Create all 3 chapters for Module 2
- [ ] Create all 3 chapters for Module 3
- [ ] Create all 3 chapters for Module 4

### Task 4: Frontmatter Application
- [ ] Add required frontmatter to all 9 chapter files
- [ ] Ensure unique IDs for each document
- [ ] Set proper sidebar positions (1, 2, 3 per module)

---

## Phase 3: Validation & Testing

### Gate 1: Architecture Review
- [ ] All directories created successfully
- [ ] Directory names match specification
- [ ] No extra or missing directories

### Gate 2: Content Contract
- [ ] All chapter files have proper frontmatter
- [ ] All IDs are unique
- [ ] Sidebar positions are correct (1, 2, 3 per module)

### Gate 3: Integration Test
- [ ] Sidebar renders correctly with new modules
- [ ] Navigation shows all 4 modules (1-4) in correct order
- [ ] All chapters are accessible through sidebar

### Gate 4: Final Validation
- [ ] All files are `.md` format (no MDX)
- [ ] Module ordering is correct (2, 3, 4 after existing Module 1)
- [ ] No backward dependencies between modules
- [ ] All content follows conceptual/architectural focus

---

## Risk Analysis

**High Risk Items**:
- Sidebar configuration conflicts with existing setup
- ID collisions in frontmatter
- Incorrect positioning causing navigation issues

**Mitigation Strategies**:
- Validate sidebar configuration before and after changes
- Use systematic ID naming convention
- Test navigation after each module addition

---

## Success Criteria

The implementation is complete when:
1. All 3 new module directories exist in `docs/`
2. All `_category_.json` files are properly configured
3. All 9 chapter files exist with correct frontmatter
4. Docusaurus sidebar shows all modules in correct order
5. All validation gates pass