from PIL import Image
from statistics import mean

from app.models.visual_profile import VisualProfile


class VisualAnalyzer:

    def analyze(self, image_path):

        image = Image.open(image_path)

        width, height = image.size

        orientation = (
            "Portrait"
            if height >= width
            else "Landscape"
        )

        aspect_ratio = round(width / height, 3)

        gray = image.convert("L")

        brightness = round(
            mean(gray.getdata()),
            2
        )

        color_mode = image.mode

        return VisualProfile(
            width=width,
            height=height,
            orientation=orientation,
            aspect_ratio=aspect_ratio,
            color_mode=color_mode,
            average_brightness=brightness,
        )