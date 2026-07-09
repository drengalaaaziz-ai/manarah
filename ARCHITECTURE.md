# MANARAH Architecture

## Vision

MANARAH is not a PDF reader.

MANARAH is an Arabic Knowledge Operating System that transforms books into structured knowledge.

---

# Architecture Decision Records (ADR)

## ADR-001

### Title
Pages are the fundamental processing unit.

### Decision
Every page is processed independently.

The system never assumes the existence of:
- Table of Contents
- Chapters
- Lessons
- Index

These structures are discovered after page analysis.

---

## ADR-002

### Title
No information is accepted as truth without verification.

### Decision
Every extracted piece of information must be supported by one or more independent evidence sources.

Examples of evidence:

- OCR text
- Visual heading detection
- Font size
- Page layout
- Table of contents (optional)
- Cross-page consistency

The system combines evidence before accepting knowledge.

---

## ADR-003

### Title
Every architectural decision must scale to one million books.

### Decision
Before implementing any feature, ask:

"Will this design still work for one million different books?"

If the answer is "No", redesign it.