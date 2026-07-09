from dataclasses import dataclass
from pathlib import Path
from datetime import datetime


@dataclass
class Book:

    # معرف دائم داخل MANARAH
    book_id: str

    # اسم الملف الأصلي
    filename: str

    # عنوان الكتاب (يستخرج لاحقاً)
    title: str

    # المؤلف
    author: str

    # المجال المعرفي
    domain: str

    # لغة الكتاب
    language: str

    # المسار الأصلي
    source_path: Path

    # عدد الصفحات
    pages: int

    # وقت الإدخال
    created_at: datetime