from pathlib import Path

from PIL import Image, ImageFilter, ImageOps


class ImagePreprocessor:
    """
    يحسن الصورة قبل OCR.
    """

    def process(self, input_path, output_path):

        input_path = Path(input_path)
        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        image = Image.open(input_path)

        # تحويل إلى تدرج رمادي
        image = ImageOps.grayscale(image)

        # زيادة التباين تلقائياً
        image = ImageOps.autocontrast(image)

        # إزالة الضوضاء البسيطة
        image = image.filter(ImageFilter.MedianFilter())

        # زيادة الحدة
        image = image.filter(ImageFilter.SHARPEN)

        image.save(output_path)

        return output_path