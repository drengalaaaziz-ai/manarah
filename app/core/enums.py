from enum import Enum


class DocumentType(Enum):

    PDF = "PDF"

    WORD = "WORD"

    IMAGE = "IMAGE"


class Language(Enum):

    ARABIC = "Arabic"

    ENGLISH = "English"

    UNKNOWN = "Unknown"