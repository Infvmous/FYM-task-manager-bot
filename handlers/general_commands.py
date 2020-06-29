from aiogram import types
from loader import dp, db


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    user_id = message.chat.id
    if db.user_exists(user_id, 2):
        await message.answer('Добавить новую задачу /add')   
    elif db.user_exists(user_id, 3):
        await message.answer('Админ')
    elif db.user_exists(user_id, 1):
        await message.answer('✔️ Доступ получен, права фармера')
        user_commands = """
Обновить статус задачи /update
Список новых задач /new
Список задач в работе /inwork
Список выполненных задач /done"""
        await message.answer(user_commands)
    else:
        await message.answer(f'Здравствуй @{message.chat.username} -> #{user_id}')