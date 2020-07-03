from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db
from keyboards.inline.callback_data import status_callback


async def statuses_keyboard(task_id):
    """ Generate inline keyboard with statuses from database

    Args:
        task_id (int): task id

    Returns:
        markup[?]: iniline keybaord markup with statuses
    """
    statuses = db.get_statuses(True)
    keyboard = InlineKeyboardMarkup(row_width=2)
    for status in statuses:
        btn = InlineKeyboardButton(text=status[1], callback_data=status_callback.new(
            status_id=f'#{status[0]}', task_id=task_id
        ))
        keyboard.insert(btn)
    return keyboard

