import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
DB = os.getenv('DB')
CHANNEL_ID = os.getenv('CHANNEL_ID')