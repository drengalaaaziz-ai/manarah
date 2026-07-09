from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass
class Book:
    title: str
    path: Path
    pages: int
    language: str = "Unknown"
    needs_ocr: bool = False


@dataclass
class Lesson:
    title: str
    order: int


@dataclass
class Concept:
    title: str
    description: str


@dataclass
class Rule:
    title: str
    description: str


@dataclass
class Example:
    sentence: str
    explanation: str


@dataclass
class Exercise:
    question: str
    answer: str | None = None


@dataclass
class KnowledgeGraph:

    books: List[Book] = field(default_factory=list)

    lessons: List[Lesson] = field(default_factory=list)

    concepts: List[Concept] = field(default_factory=list)

    rules: List[Rule] = field(default_factory=list)

    examples: List[Example] = field(default_factory=list)

    exercises: List[Exercise] = field(default_factory=list)