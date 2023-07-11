import os

DB_PATH = os.path.join(os.environ.get('ALFIS_DB_PATH'), os.environ.get('ALFIS_DB_FILE'))

API_TOKEN = os.environ.get('BOT_API_TOKEN')

REQUEST = "SELECT MAX(id) FROM blocks;"

SECONDS = int(os.environ.get('SCHEDULE_SECONDS'))

TEXT_MSG = "Last Alfis Block is: "

#DB_MONGO_NAME = 'aiogram_fsm'

#DB_PORT = 27017

#DB_HOST = os.environ.get('MONGO_SRV')

DB_FILE = 'chat_ids.db'

DB_TABLE = 'chat_ids'

DB_COL = 'ids'

REQ_TIME_LAST_BLOCK = "SELECT MAX(timestamp) FROM blocks;"
