import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = [641603995]  # твій Telegram ID

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")
