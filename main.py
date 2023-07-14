import logging
import time
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import get_last_block, get_chat_ids, save_chat_id, get_next_block
from config import SECONDS, TEXT_MSG, API_TOKEN, ALERT_TIME, TEXT_ALERT_MSG

LAST_BLOCK = ""

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

scheduler = AsyncIOScheduler()
alert = AsyncIOScheduler()

@dp.message_handler(commands=['start', 'get'])
async def send_welcome(message: types.Message):
    global LAST_BLOCK

    if not LAST_BLOCK:
        scheduler.start()

    LAST_BLOCK =  get_last_block()
    logging.info(f'command: [start, get], user: {message.from_user.id}, chat_id: {message.chat.id}, last_block: {LAST_BLOCK[2]}')
    save_chat_id(message.chat.id)
    await message.reply(f'{TEXT_MSG}{LAST_BLOCK[2]}')

async def schedule_last_block(bot: Bot):

    global LAST_BLOCK
  
    if (cur_block := get_last_block())[2] == LAST_BLOCK[2]:
        if int(time.time()) - cur_block[1] >= ALERT_TIME and cur_block[0]:
            for chat_id in get_chat_ids():
                await bot.send_message(text=TEXT_ALERT_MSG.format(cur_block[2]), chat_id=chat_id)
                logging.info(f'schedule: Chat_ID: {chat_id}, ALERT Old block with data > 10min: {cur_block[2]}')
        elif int(time.time()) - cur_block[1] >= ALERT_TIME and cur_block[2] % 5:
            for chat_id in get_chat_ids():
                await bot.send_message(text=TEXT_ALERT_MSG.format(cur_block[2]), chat_id=chat_id)
                logging.info(f'schedule: Chat_ID: {chat_id}, ALERT Old block with sing > 10min: {cur_block[2]}')
        else:
            logging.info('schedule: No new blocks')
    else:
        for chat_id in get_chat_ids():
            await bot.send_message(text=f'{TEXT_MSG}{cur_block[2]}', chat_id=chat_id)
            logging.info(f'schedule: Chat_ID: {chat_id}, New block is: {cur_block[2]}')
            
        LAST_BLOCK = cur_block
        
  
scheduler.add_job(schedule_last_block, "interval", seconds=SECONDS, args=(bot,))

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
