import config
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db import Db


# Setup lvl of logs
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Database connection
db = Db(config.DB)

