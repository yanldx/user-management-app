from app import engine
from sqlalchemy import text

print("🧪 Connecting to:", engine.url)
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("✅ Connected! Result:", result.scalar())
    