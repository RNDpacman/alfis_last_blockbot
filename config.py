import os

DB_ALFIS_PATH = os.path.join(os.environ.get('ALFIS_DB_PATH', '.'), os.environ.get('ALFIS_DB_FILE', 'blockchain.db'))

API_TOKEN = os.environ.get('BOT_API_TOKEN', 'token')

CHECK_SECONDS = int(os.environ.get('SCHEDULE_SECONDS', 50))

ALERT_SECONDS = int(os.environ.get('ALERT_SECONDS', 180))

ALERT_TIME = int(os.environ.get('ALERT_TIME', 600))

TEXT_MSG = "Last Alfis Block is: "

TEXT_5_MSG = "Block #{} multiple of 5"

TEXT_ALERT_MSG = """Внимание!  @Revertron, @R4SAS и @dradanudanay
После блока с данными/подписями #{} более {} минут не приходят блоки с подписями!"""

DB_FILE = 'support.db'


