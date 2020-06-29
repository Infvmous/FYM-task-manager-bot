from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db
from helper import remove_special_symbols


tasks = db.get_tasks() # Get all tasks from database
tasks_keyboard = ReplyKeyboardMarkup()
for task in tasks:
    # Получить статус заказа
    status = remove_special_symbols(str(db.get_status_name(task[3])))
    tasks_keyboard.insert(KeyboardButton(f'#{task[0]} "{task[1]}" - {status}'))