from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db, dp
from keyboards.inline.callback_data import status_callback

# Get all statuses from db
statuses = db.get_statuses(True)

# Create keyboards
statuses_keyboard = InlineKeyboardMarkup()

# Add statuses to buttons
row_btns = (InlineKeyboardButton(
    text=status, callback_data=status_callback.new(
        user_id=''
    )) for status_id, status in statuses)

# Add buttons with statuses to keyboard
statuses_keyboard.row(*row_btns)