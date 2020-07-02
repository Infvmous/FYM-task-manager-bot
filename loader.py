import config
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from database.db import Database as Db


# Setup logs level
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Bot init
bot = Bot(token=config.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Database connection
db = Db(config.DB_FILE)

