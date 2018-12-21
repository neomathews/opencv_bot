import os
import random
import telepot
from telepot.loop import MessageLoop
import config

TOKEN = config.token
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if command == '/image':
        bot.sendPhoto(chat_id, 'https://picsum.photos/200/300/?random')
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_forever()
