from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db, bot
from config import CHANNEL_ID

from misc.states import AddUser
from misc.roles import roles_dict
from misc.helper import send_message_to_telegram, remove_special_symbols, \
    collect_string_in_dict

import logging
import re


@dp.message_handler(Command('user'), state='*')
async def add_user_step_1(message: Message):
    """ Ввод телеграм id юзера """
    user_id = message.chat.id
    # If user exists and he is admin
    if db.user_exists(user_id, 3):
        await AddUser.user_info.set()
        msg = '''
📝 Добавление нового пользователя\n
Введи информацию о пользователе в формате:
телеграм_id(цифры):имя_пользователя(латиница/цифры):полное_имя(кириллица/латинский):роль_id(1,2,3)\n
Например: 1337228:username:Вася Пупкин:2\n
Роли
1 - Фармер
2 - Медиа-баер
3 - Администратор'''
        await message.answer(msg) 
    else:
        await message.answer('❌ Недостаточно прав')


@dp.message_handler(state=AddUser.user_info)
async def add_user_step_2(message: Message, state: FSMContext):
    """ Обработка введенной информации о пользователе """
    user_info = message.text
    pattern = r'([\d]+:[\da-zA-Z]+:[a-zA-Zа-яА-Я\s]+:[123])'
    if re.fullmatch(pattern, user_info):
        user_info = user_info.split(':')
        user_id = user_info[0]
        username = user_info[1]
        full_name = user_info[2]
        role_id = user_info[3]
        role_in_db = await remove_special_symbols(db.get_role(role_id))
        role = roles_dict.get(role_in_db)
        if db.add_user(user_id, username, full_name, role_id):
            msg = f'📰 Добавлен новый пользователь @{username} с правами доступа "{role}"'
            await message.answer(msg)
            await send_message_to_telegram(msg)
        else:
            await message.answer(f'❌ Произошла ошибка при добавлении пользователя в систему')
    else:
        await message.answer(f'❌ Введенная строка не соответствует регулярному\
            выражению {pattern}')
    await state.finish()
