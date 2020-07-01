from config import CHANNEL_ID
from loader import bot, db
import re

from keyboards.inline.status_buttons import statuses_keyboard


async def remove_special_symbols(string):
    """ Remove special symbols from string """
    alphanumeric = [character for character in string if character.isalnum()]
    alphanumeric = ''.join(alphanumeric)
    return alphanumeric


async def send_message_to_telegram(msg, task_id = None, to_channel = True):
    """ Отправить сообщение если задача добавлена в базу данных """ 
    if to_channel:
        await bot.send_message(CHANNEL_ID, msg)
    else:
        if task_id is not None:
            users = db.get_users()
            for user in users:
                await bot.send_message(user[0], msg,
                    reply_markup=await statuses_keyboard(task_id)) # Клавиатура с выбором статуса


async def collect_string_in_dict(string):
    string = string.split(':')
    tg_id = string[0]
    username = string[1]
    full_name = string[2]
    role = string[3]
    
    id_pattern = r'[\d]'
    username_pattern = r'[a-z]'
    role_pattern = r'[1,2,3]'


async def check_expression(string, pattern):
    if re.match(string, pattern):
        return True