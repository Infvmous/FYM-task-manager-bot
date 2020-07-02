from aiogram import types
from loader import dp, db


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    user_id = message.chat.id
    if db.user_exists(user_id, 2):
        await message.answer('Добавить новую задачу /add')   
    elif db.user_exists(user_id, 3):
        admin_commands = """
Добавить новую задачу /add
Добавить пользователя /user"""
        await message.answer(admin_commands)
    elif db.user_exists(user_id, 1):
        await message.answer('✔️ Доступ получен, права фармера')
        user_commands = """
Обновить статус задачи /update
Список новых задач /new
Список задач в работе /inwork
Список выполненных задач /done
*** В РАЗРАБОТКЕ ***"""
        await message.answer(user_commands)
    else:
        await message.answer(f'{user_id}:{message.chat.username}:{message.chat.full_name}')