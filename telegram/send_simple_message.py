#!/usr/bin/env python3
from datetime import datetime
import time

import telegram

# https://core.telegram.org/bots#generating-an-authorization-token
token = ''
bot = telegram.Bot(token=token)


def send(msg, chat_id):
    """
    send a specific message to user.

    chat_id: id to send a sendMessage.
    Example group: https://web.telegram.org/#/im?p=g111111111, chat_id is:
    '-111111111'
    """
    bot.sendMessage(chat_id=chat_id, text=msg)


if __name__ == '__main__':
    chat_id = ''
    while True:
        message = f'Current date and UTC time: {datetime.utcnow().isoformat()}'
        send(message, chat_id)
        time.sleep(30)
