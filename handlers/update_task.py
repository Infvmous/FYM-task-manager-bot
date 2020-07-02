from aiogram.types import CallbackQuery

from loader import dp, db, bot
from config import CHANNEL_ID

from misc.helper import remove_special_symbols

import logging


@dp.callback_query_handler(text_contains='#')
async def process_callback_status(call: CallbackQuery):
    """ Метод обработки инлайн кнопок для изменения статуса задач """
    await call.answer(cache_time=60)
    callback_data = call.data.split(':')
    logging.info(f'call = {callback_data}')
    # Get status name
    status_id = await remove_special_symbols(callback_data[1])
    status = db.get_status(status_id)[0][1]
    # Get task name
    task_id = callback_data[2]
    task = db.get_task(task_id)[0][1]
    # Telegram username of user pressed one of the btns
    username = call.message.chat.username
    # Ответ на нажатие Inline кнопки
    if db.update_status(task_id, status_id):
        msg = f'@{username} установил статус "{status}" для задачи "{task}"'
        await call.message.answer(msg)
        await bot.send_message(CHANNEL_ID, msg)




