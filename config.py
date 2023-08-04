import os

DB_ALFIS_PATH = os.path.join(os.environ.get('ALFIS_DB_PATH', '.'), os.environ.get('ALFIS_DB_FILE', 'blockchain.db'))

API_TOKEN = os.environ.get('BOT_API_TOKEN', 'token')

# частота провеки блоков
CHECK_SECONDS = int(os.environ.get('SCHEDULE_SECONDS', 64))

# частота поторений сообщения о тревоге
ALERT_SECONDS = int(os.environ.get('ALERT_SECONDS', 1024))

# через сколько секунд после последнего блока запускать тревогу
ALERT_TIME = int(os.environ.get('ALERT_TIME', 600))

# текст сообщения о номере текущего блока
TEXT_MSG = "Last Alfis Block is: "

# текст сообщения если блок кратен 5
TEXT_5_MSG = "Block #{} multiple of 5"

TEXT_ALERT_MSG = """Внимание!  @Revertron, @R4SAS, @dradanudanay и другие многоуважаемые Доны.
После блока с данными/подписями #{} более {} минут не приходят блоки с подписями!"""

DB_FILE = 'support.db'


