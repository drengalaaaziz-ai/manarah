from dataclasses import dataclass


@dataclass(slots=True)
class VisualProfile:
    """
    الخصائص البصرية للصفحة.
    """

    width: int

    height: int

    orientation: str

    aspect_ratio: float

    color_mode: str

    average_brightness: float