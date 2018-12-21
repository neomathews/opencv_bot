import os
import telepot
from telepot.loop import MessageLoop
import pprint
import cv2 as cv
import tempfile
import config

TOKEN = config.token
def handle(msg):
    if msg["photo"]:
        chat_id = msg['chat']['id']
        f = tempfile.NamedTemporaryFile(delete=True).name+".png"
        photo = msg['photo'][-1]["file_id"]
        path = bot.getFile(photo)["file_path"]
        bot.sendMessage(chat_id, "Retrieving %s" % path)
        bot.download_file(photo, f)
        p = cv.imread(f)
        gray = cv.cvtColor(p, cv.COLOR_BGR2GRAY)
        cv.imwrite(f, gray)
        bot.sendPhoto(chat_id, open(f, 'rb'))
    else:
        print("no photo")
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_forever()
