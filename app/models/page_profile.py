from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class PageProfile:
    """
    يمثل صفحة واحدة داخل النظام.
    """

    page_number: int

    image_path: Path

    width: float

    height: float

    dpi: int = 300

    ocr_text: str = ""

    cleaned_text: str = ""

    language: str = "Unknown"

    page_type: str = "Unknown"

    lesson_title: str | None = None

    concepts: list[str] = field(default_factory=list)

    rules: list[str] = field(default_factory=list)

    examples: list[str] = field(default_factory=list)

    exercises: list[str] = field(default_factory=list)

    relations: list[dict] = field(default_factory=list)

    confidence: dict = field(default_factory=dict)