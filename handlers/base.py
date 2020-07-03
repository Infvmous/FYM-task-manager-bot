import logging

from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.utils.markdown import hbold, hlink, quote_html

from loader import dp, db, bot
from utils.helper import notify_channel


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    msg = f'{message.from_user.id}:{message.chat.username}:{message.chat.full_name}\n\
        /help - Список команд'
    await message.answer(f'{message.from_user.id}:{message.chat.username}:{message.chat.full_name}')


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    user_id = message.from_user.id
    user = db.get_user(user_id)
    user_group = user[4] if user is not None else None
    text = [
        '{cmd} - Информация о себе'.format(cmd='/start'),
        '{cmd} - Мои команды'.format(cmd='/help')
    ]
    print(f'grp: {user_group}')
    if user_group == 1: # User
        pass
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
                '{cmd} - Список всех активных аккунтов'.format(cmd='/accs'),
                '{cmd} - Добавить нового пользователя'.format(cmd='/user'),
                '{cmd} - Отчет по выполненным задачам за месяц'.format(cmd='/done'),
                '{cmd} - Задачи в работе'.format(cmd='/inwork')
            ]
        )
    await message.answer('\n'.join(text))
