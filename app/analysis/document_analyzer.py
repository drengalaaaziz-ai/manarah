from app.models.document_profile import DocumentProfile


class DocumentAnalyzer:
    """
    يقوم بتحليل الوثيقة وإضافة استنتاجات ذكية.
    """

    def analyze(self, profile: DocumentProfile) -> DocumentProfile:

        # تحديد اللغة (سنطورها لاحقًا)
        profile.language = "Arabic"

        # تحديد نوع الوثيقة
        if profile.contains_images and not profile.contains_text:
            profile.document_type = "Scanned PDF"

        elif profile.contains_text:
            profile.document_type = "Digital PDF"

        else:
            profile.document_type = "Unknown"

        return profile