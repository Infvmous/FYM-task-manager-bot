from config import CHANNEL_ID
from loader import bot, db

from keyboards.inline.status_buttons import statuses_keyboard


async def remove_special_symbols(string):
    """ Remove special symbols in string

    Args:
        string (string): any string

    Returns:
        string: string without any special symbols
    """
    alphanumeric = [character for character in str(string) if character.isalnum()]
    alphanumeric = ''.join(alphanumeric)
    return alphanumeric


async def send_message_to_telegram(msg, task_id = None, to_channel = True): 
    """ Send message to all users or telegram channel

    Args:
        msg (varchar): message which need to deliver
        task_id (int, optional): task id. Defaults to None.
        to_channel (bool, optional): If true deliver to channel, False - to all users. Defaults to True.
    """
    if to_channel:
        await bot.send_message(CHANNEL_ID, msg)
    else:
        if task_id is not None:
            users = db.get_users()
            for user in users:
                await bot.send_message(user[0], msg,
                    reply_markup=await statuses_keyboard(task_id)) # Statuses keyboard


async def replace_special_symbols(string):
    """ Replacing specific chars from string

    Args:
        string (string): any string

    Returns:
        string: string with replaced chars
    """
    chars = "[(,)]"
    for char in chars:
        string = string.replace(char, '')
    return string