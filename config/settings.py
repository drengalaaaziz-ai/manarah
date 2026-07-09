from dataclasses import dataclass


@dataclass
class Settings:

    PROJECT_NAME = "MANARAH"

    VERSION = "0.1.0"

    DEFAULT_LANGUAGE = "Arabic"

    OCR_ENGINE = "PaddleOCR"

    SAVE_INTERMEDIATE_RESULTS = True

    EXPORT_JSON = True

    EXPORT_GRAPH = True


settings = Settings()