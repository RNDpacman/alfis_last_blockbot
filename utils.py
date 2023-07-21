import sqlite3
from config import DB_FILE, DB_ALFIS_PATH, ALERT_TIME, TEXT_ALERT_MSG

def get_last_block():
    with sqlite3.connect(DB_ALFIS_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT timestamp, id FROM blocks ORDER BY id DESC LIMIT 1;")
        res = cursor.fetchone()
        return {
                    'timestamp': res[0],
                    'id': res[1]
                }

def save_block_bookmark(block):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT INTO delayed_blocks (num, timestamp) VALUES (?, ?)''', (block['id'], block['timestamp']))
        except sqlite3.IntegrityError:
            print('Duplicate bookmark block')    
        conn.commit()

def get_block_bookmark():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT num, timestamp FROM delayed_bloks ORDER BY num DESC LIMIT 1''')
        return {
                    'id': cursor.fetchone()[0],
                    'timestamp': cursor.fetchone()[1]
                }
        
def save_chat_id(chat_id: int):
    '''
    Save chat id 
    '''
    with sqlite3.connect(DB_FILE) as conn:

        cursor = conn.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS chats (
                            id INTEGER PRIMARY KEY,
                            chat_id INTEGER,
                            UNIQUE (chat_id)
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS delayed_blocks (
                            id INTEGER PRIMARY KEY,
                            num INTEGER,
                            timestamp INTEGER,
                            UNIQUE (num)
                        )''')
        try:
            cursor.execute(f'INSERT INTO chats (chat_id) VALUES (?)', (chat_id,))
        except sqlite3.IntegrityError:
            print('оооо бля хуйню делаешь!')

        conn.commit()

def get_chat_ids():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT chat_id FROM chats')
        for row in cursor.fetchall():
            yield row[0]

