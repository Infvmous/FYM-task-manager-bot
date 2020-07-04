from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db
from keyboards.inline.callback_data import status_callback


async def statuses_keyboard(task_id):
    statuses_dict = {
        'В работе': 'Взять в работу',
        'Пожилая': 'Выполнил',
    }
    statuses = db.get_task_statuses(1)
    keyboard = InlineKeyboardMarkup()
    for status in statuses:
        btn = InlineKeyboardButton(text=statuses_dict.get(status[1]),
            callback_data=status_callback.new(
                status_id=f'#{status[0]}', task_id=task_id
            ))
        keyboard.insert(btn)
    return keyboard

