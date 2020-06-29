from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db
from keyboards.inline.callback_data import status_callback


async def statuses_keyboard(task_id, username):
    # Get all statuses from db
    statuses = db.get_statuses(True)
    keyboard = InlineKeyboardMarkup(row_width=2)
    for status in statuses:
        btn = InlineKeyboardButton(text=status[1], callback_data=status_callback.new(
            status_id=f'#{status[0]}', task_id=task_id, set_by=username
        ))
        keyboard.insert(btn)
    return keyboard

