import os

API_ID    = os.environ.get("API_ID", "21546895")
API_HASH  = os.environ.get("API_HASH", "3fbb1254728cf2ab3447a0e9e7aa6fc0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8126756346:AAEXK0MQQu-pAll5em1c1dULSmXdYYrCOSs") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
