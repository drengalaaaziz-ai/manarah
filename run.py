from config.settings import settings
from app.pipeline.pipeline import ManarahPipeline


print("=" * 60)
print(settings.PROJECT_NAME)
print("Version:", settings.VERSION)
print("=" * 60)

pipeline = ManarahPipeline("books/qawaed.pdf")

pipeline.execute()