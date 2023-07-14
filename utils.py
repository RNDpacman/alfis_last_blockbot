import sqlite3
from config import DB_FILE, DB_TABLE, DB_COL, DB_ALFIS_PATH, ALERT_TIME, TEXT_ALERT_MSG

def get_last_block():
    with sqlite3.connect(DB_ALFIS_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT \"transaction\", timestamp, id FROM blocks ORDER BY id DESC LIMIT 1;")
        return cursor.fetchone()


def get_next_block(last_block: int):
    with sqlite3.connect(DB_ALFIS_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT timestamp, id FROM blocks WHERE id > {last_block} LIMIT 1")
        return cursor.fetchone()

def save_chat_id(chat_id: int):
    '''
    Save last block on the bd
    '''
    with sqlite3.connect(DB_FILE) as conn:

        cursor = conn.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {DB_TABLE} (
                            id INTEGER PRIMARY KEY,
                            {DB_COL} INTEGER,
                            UNIQUE ({DB_COL})
                        )''')
        try:
            cursor.execute(f'INSERT INTO {DB_TABLE} ({DB_COL}) VALUES (?)', (chat_id,))
        except sqlite3.IntegrityError:
            print('оооо бля хуйню делаешь!')

        conn.commit()

def get_chat_ids():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT {DB_COL} FROM {DB_TABLE}')
        for row in cursor.fetchall():
            yield row[0]

