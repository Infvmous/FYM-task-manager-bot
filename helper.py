from config import CHANNEL_ID
from loader import bot, db
from keyboards.inline.status_buttons import statuses_keyboard


def remove_special_symbols(string):
    """ Remove special symbols from string """
    alphanumeric = [character for character in string if character.isalnum()]
    alphanumeric = ''.join(alphanumeric)
    return alphanumeric


async def send_message_to_telegram(task, username, task_id, to_channel = True):
    """ Отправить сообщение если задача добавлена в базу данных """
    msg = f'👀 Новая задача "{task}" была добавлена пользователем @{username}'
    if to_channel:
        await bot.send_message(CHANNEL_ID, msg)
    elif not to_channel:
        users = db.get_users()
        for user in users:
            await bot.send_message(user[0], msg,
                reply_markup=await statuses_keyboard(task_id))