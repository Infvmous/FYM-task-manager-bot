from aiogram import types
from loader import dp, db


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    user_id = message.chat.id
    if db.user_exists(user_id, True):
        await message.answer('Add new task /task')   
    else:
        await message.answer(f'Hello @{message.chat.username} - {user_id}')