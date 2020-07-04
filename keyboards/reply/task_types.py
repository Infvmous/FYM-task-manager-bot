from loader import db
from config import TYPES_TABLE
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def task_types():
    types = db.get_all(TYPES_TABLE)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2,
        one_time_keyboard=True)
    markup.add(*(KeyboardButton(task_type[1]) for task_type in types))
    return markup

