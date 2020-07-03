import logging

from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.utils.markdown import hbold, hlink, quote_html

from loader import dp, db, bot
from utils.helper import notify_channel
from config import USERS_TABLE


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('/help - Список команд') 
    if db.get_where(USERS_TABLE, message.from_user.id) is None:
        msg = f'♿️ {message.from_user.id}:{message.chat.username}:{message.chat.full_name}'
        await notify_channel(msg)


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    user_id = message.from_user.id
    user = db.get_where(USERS_TABLE, user_id)
    user_group = user[3] if user is not None else None
    text = []
    if user_group == 1: text.extend(['♿️ Пожилым фармерам не нужны команды'])
    elif user_group == 2: # Customer  
        text.extend(
            [
                '{cmd} - Выдать новую задачу'.format(cmd='/task'),  
                '{cmd} - Мои аккаунты'.format(cmd='/accs')
            ]
        )
    elif user_group == 3: # Admin
        text.extend(
            [
                '{cmd} - Выдать новую задачу'.format(cmd='/task'),  
                '{cmd} - Активные аккаунты'.format(cmd='/accs'),
                '{cmd} - Добавить нового пользователя'.format(cmd='/user'),
                '{cmd} - Выполненные задачи за месяц'.format(cmd='/done'),
                '{cmd} - Задачи в работе'.format(cmd='/inwork')
            ]
        )
    else: text.extend(['🚷 Доступных команд не найдено'])
    await message.answer('\n'.join(text))


@dp.errors_handler()
async def errors_handler(update: types.Update, exception: Exception):
    try:
        raise exception
    except Exception as e:
        logging.exception("Cause exception {e} in update {update}", e=e, update=update)
    return True
