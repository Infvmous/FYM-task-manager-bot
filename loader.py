import logging
import config

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from database.db import Database as Db


# Logs
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = Bot(token=config.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Db(config.DB_FILE)