from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db


def statuses_keyboard(status_tuple):
    status_id = status_tuple[0][0]
    statuses = db.get_statuses(status_id)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for status in statuses:
        keyboard.insert(KeyboardButton(status[1]))
    return keyboard