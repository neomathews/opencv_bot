import telepot
import os
import pprint
import config

TOKEN = config.token
bot = telepot.Bot(TOKEN)
pprint.pprint(bot.getMe())
