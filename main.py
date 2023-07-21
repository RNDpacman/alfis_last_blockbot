import logging
import time
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import get_last_block, get_chat_ids, save_chat_id, get_block_bookmark, save_block_bookmark
from config import CHECK_SECONDS, TEXT_MSG, API_TOKEN, ALERT_TIME, ALERT_SECONDS, TEXT_ALERT_MSG, TEXT_5_MSG

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

check_block_sched = AsyncIOScheduler()
alert_block_sched = AsyncIOScheduler()

@dp.message_handler(commands=['start', 'get'])
async def send_welcome(message: types.Message):
    
    last_block = get_last_block()
    
    logging.info(f'command: [start, get], user: {message.from_user.id}, chat_id: {message.chat.id}, last_block: {last_block["id"]}')
    save_chat_id(message.chat.id)
    await message.reply(f'{TEXT_MSG}{last_block["id"]}')


@dp.message_handler(commands=['config'])
async def send_welcome(message: types.Message):
    await message.reply(f'''CHECK_SECONDS: {CHECK_SECONDS}\nALERT_TIME: {ALERT_TIME}\nALERT_SECONDS: {ALERT_SECONDS}''')

async def check_last_block(bot: Bot):

    last_block = get_last_block()
    
    if last_block['id'] % 5 == 0 and last_block['id'] != get_block_bookmark()['id']:
        save_block_bookmark(last_block)
        for chat_id in get_chat_ids():
            await bot.send_message(text=TEXT_5_MSG.format(last_block['id']), chat_id=chat_id)
            logging.info(f'schedule: Chat_ID: {chat_id}, block: {last_block["id"]} % 5 == 0')
        
    
    if last_block['id'] % 5 and int(time.time()) - last_block['timestamp'] > ALERT_TIME:
        save_block_bookmark(last_block)
        if not alert_block_sched.running:
            alert_block_sched.start()    
    else:
        
        if alert_block_sched.running:
            alert_block_sched.shutdown()

  
async def alert_block(bot: Bot):
    last_block = get_block_bookmark()
    for chat_id in get_chat_ids():
        await bot.send_message(text=TEXT_ALERT_MSG.format(last_block['id'], ALERT_TIME/60), chat_id=chat_id)
        logging.info(f'schedule: Chat_ID: {chat_id}, ALERT Next block after block {last_block["id"]} delayed')
    
check_block_sched.add_job(check_last_block, "interval", seconds=CHECK_SECONDS, args=(bot,))
alert_block_sched.add_job(alert_block, "interval", seconds=ALERT_SECONDS, args=(bot,))   

if not check_block_sched.running:
    save_block_bookmark({'id': False, 'timestamp': False}) # что бы не ругался на не созданную таблицу при вызове get_block_bookmark()
    check_block_sched.start()
    
  
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
   
