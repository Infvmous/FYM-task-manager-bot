import os
from dotenv import load_dotenv


load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
DB_FILE = os.getenv('DB_FILE')
CHANNEL_ID = os.getenv('CHANNEL_ID')

STATUSES_TABLE1 = os.getenv('STATUSES_TABLE1')
ACCS_TABLE = os.getenv('ACCS_TABLE')
GRPS_TABLE = os.getenv('GRPS_TABLE')
STATUSES_TABLE2 = os.getenv('STATUSES_TABLE2')
TASKS_TABLE = os.getenv('TASKS_TABLE')
TYPES_TABLE = os.getenv('TYPES_TABLE')
USERS_TABLE = os.getenv('USERS_TABLE')
