import sqlite3
from pymongo import MongoClient
from config import REQUEST, DB_PORT, DB_HOST, DB_MONGO_NAME

def get_last_block(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(REQUEST)
    last_block = cursor.fetchall()[0][0]
    conn.close()
    return last_block



def get_chat_ids():
    '''
    Возвращает генератор id чатов с которыми бот работал
    '''
    client = MongoClient(f'mongodb://{DB_HOST}:{DB_PORT}/')
    db = client[DB_MONGO_NAME]
    collection = db['aiogram_data']
    chats = collection.find({})
    for chat_id in chats:
        yield chat_id['chat']


