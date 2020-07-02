from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db
from config import CHANNEL_ID

from misc.states import AddUser
from misc.helper import send_message_to_telegram, remove_special_symbols, \
    replace_special_symbols

import re


@dp.message_handler(Command('user'), state='*')
async def add_user_step_1(message: Message):
    """ /user command. First step of user creation state

    Args:
        message (Message): telegram api
    """
    user_id = message.chat.id
    # If user exists and he is admin
    if db.user_exists(user_id, 3):
        await AddUser.user_info.set()
        await message.answer('''
📝 Добавление нового пользователя\n
Введи информацию о пользователе в формате:
телеграм_id:имя_пользователя:полное_имя:роль_id\n
Например: 1337228:username:Вася Пупкин:2\n
Роли
1 - Фармер
2 - Медиа-баер
3 - Администратор''') 
    else:
        await message.answer('❌ Недостаточно прав')


@dp.message_handler(state=AddUser.user_info)
async def add_user_step_2(message: Message, state: FSMContext):
    """ /user command. User input processing.

    Args:
        message (Message): telegram api
        state (FSMContext): state data
    """
    user_info = message.text # user data
    pattern = r'([\d]+:[\da-zA-Z]+:[a-zA-Zа-яА-Я\s]+:[123])' #regEx for user data checking
    if re.fullmatch(pattern, user_info):
        user_info = user_info.split(':')
        # collect user data from tuple to variables
        user_id = user_info[0]
        username = user_info[1]
        full_name = user_info[2]
        role_id = user_info[3]
        role = db.get_role(role_id) # role description
        role = await replace_special_symbols(role)
        print(f'role - {role}')
        if db.add_user(user_id, username, full_name, role_id):
            msg = f'📰 Добавлен новый пользователь @{username} с правами доступа {role}'
            await message.answer(msg)
            await send_message_to_telegram(msg)
        else:
            await message.answer(f'❌ Произошла ошибка при добавлении пользователя в систему')
    else:
        await message.answer(f'❌ Введенная строка не соответствует регулярному выражению {pattern}')
    await state.finish()
