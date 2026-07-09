class ManarahError(Exception):
    """Base Exception"""


class BookNotFoundError(ManarahError):
    pass


class OCRRequiredError(ManarahError):
    pass