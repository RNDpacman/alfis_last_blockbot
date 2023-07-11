import sqlite3
import time
#from pymongo import MongoClient
#from config import REQUEST, DB_PORT, DB_HOST, DB_MONGO_NAME
from config import REQUEST, DB_FILE, DB_TABLE, DB_COL

def get_last_block(db):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute(REQUEST)
        return cursor.fetchall()[0][0]

def get_last_time_block(db):
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute(REQ_TIME_LAST_BLOCK)
        return cursor.fetchall()[0][0]

#def get_chat_ids():
#    '''
#    Возвращает генератор id чатов с которыми бот работал
#    '''
#    client = MongoClient(f'mongodb://{DB_HOST}:{DB_PORT}/')
#    db = client[DB_MONGO_NAME]
#    collection = db['aiogram_data']
#    chats = collection.find({})
#    for chat_id in chats:
#        yield chat_id['chat']


def save_chat_id(chat_id: int):

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
            yield row

def check_health(last_block, time_block):
    delta_time = int(time.time()) - time_block

    if last_block % 5 == 0 and delta_time > 600:
        return false
    else:
        return true

