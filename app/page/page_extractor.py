from pathlib import Path

import fitz


class PageExtractor:
    """
    يحول صفحات PDF إلى صور.
    """

    def __init__(self, output_folder="extracted/images"):

        self.output_folder = Path(output_folder)

        self.output_folder.mkdir(parents=True, exist_ok=True)

    def extract_first_page(self, pdf_path):

        pdf = fitz.open(pdf_path)

        page = pdf.load_page(0)

        pix = page.get_pixmap(dpi=300)

        output = self.output_folder / "page_001.png"

        pix.save(output)

        pdf.close()

        return output