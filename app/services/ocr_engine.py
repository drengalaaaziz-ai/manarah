import pytesseract

from PIL import Image


class OCREngine:

    def extract_text(self, image_path):

        image = Image.open(image_path)

        text = pytesseract.image_to_string(
            image,
            lang="ara"
        )

        return text