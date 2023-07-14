import os

DB_ALFIS_PATH = os.path.join(os.environ.get('ALFIS_DB_PATH', '.'), os.environ.get('ALFIS_DB_FILE', 'blockchain.db'))

API_TOKEN = os.environ.get('BOT_API_TOKEN', 'token')

SECONDS = int(os.environ.get('SCHEDULE_SECONDS', 50))

TEXT_MSG = "Last Alfis Block is: "

TEXT_ALERT_MSG = """Внимание!  @Revertron, @R4SAS и @dradanudanay
После блока с данными или блока с подписями #{}  более 10 минут не приходят блоки с подписями!"""

DB_FILE = 'chat_ids.db'

DB_TABLE = 'chat_ids'

DB_COL = 'ids'

ALERT_TIME = 600
