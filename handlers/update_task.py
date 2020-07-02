from aiogram.types import CallbackQuery

from loader import dp, db, bot
from config import CHANNEL_ID

from misc.helper import remove_special_symbols

import logging


@dp.callback_query_handler(text_contains='#')
async def process_callback_status(call: CallbackQuery):
    """ Process status callback from inline keyboard

    Args:
        call (CallbackQuery): call to telegram api
    """
    await call.answer(cache_time=60)
    callback_data = call.data.split(':') # get callback to tuple
    logging.info(f'call = {callback_data}') # log callback
    # Get status name by id from the callback
    status_id = await remove_special_symbols(callback_data[1])
    status = db.get_status(status_id)[0][1]
    # Get task name by id from the callback
    task_id = callback_data[2]
    task = db.get_task(task_id)[0][1]
    # Telegram username of user which pressed one of the buttons
    username = call.message.chat.username
    # If user press the button and status updated send a message that
    # everying is OK.
    if db.update_status(task_id, status_id):
        msg = f'@{username} установил статус "{status}" для задачи "{task}"'
        await call.message.answer(msg)
        await bot.send_message(CHANNEL_ID, msg)




