#import logging
import sqlite3
import os

from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.contrib.fsm_storage.mongo import MongoStorage

from utils import get_last_block, get_chat_ids, save_chat_id
from config import DB_PATH, SECONDS, TEXT_MSG, API_TOKEN

PREV_BLOCK = ""

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

scheduler = AsyncIOScheduler()


@dp.message_handler(commands=['start', 'get'])
async def send_welcome(message: types.Message):
    global PREV_BLOCK

    PREV_BLOCK = cur_block = get_last_block(DB_PATH)
    logging.info(f'command: [start, get], user: {message.from_user.id}, chat_id: {message.chat.id}, last_block: {cur_block}')
    save_chat_id(message.chat.id)
    await message.reply(f'{TEXT_MSG}{cur_block}')


async def schedule_last_block(bot: Bot):

    global PREV_BLOCK

    cur_block = get_last_block(DB_PATH)
    if cur_block != PREV_BLOCK:
        PREV_BLOCK = cur_block

        for chat_id in get_chat_ids():
            await bot.send_message(text=f'{TEXT_MSG}{cur_block}', chat_id=chat_id)
            logging.info(f'schedule: Chat_ID: {chat_id}, New block is: {cur_block}')

    else:

        logging.info('schedule: No new blocks')

scheduler.add_job(schedule_last_block, "interval", seconds=SECONDS, args=(bot,))


if __name__ == '__main__':
   scheduler.start()
   executor.start_polling(dp, skip_updates=True)
