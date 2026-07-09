from dataclasses import dataclass, field

from app.models.document_profile import DocumentProfile
from app.models.page_profile import PageProfile


@dataclass(slots=True)
class KnowledgeSession:
    """
    يمثل جلسة معالجة كتاب بالكامل.
    """

    document: DocumentProfile

    pages: list[PageProfile] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)