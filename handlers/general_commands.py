from aiogram import types
from misc import dp


@dp.message_handler(commands=['start', 'help'])
async def create_task(message: types.Message):
    await message.answer('Create a task /add')