#/usr/bin/python3
from sys import argv
from telegram import Bot
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler as CQHandler
from telegram.ext import Updater
import logging
# import credentials # No longer used, BOT_TOKEN is taken from sys.argv[1]
import messages # message text is stored here
import filebase # some filenames store here
import csv # used to write persistent data

BOT_TOKEN = argv[1]
print(BOT_TOKEN)
upd = Updater(token=BOT_TOKEN, use_context=True)
disp = upd.dispatcher
logging.basicConfig(format='>%(asctime)s - %(name)s - %(levelname)s - %(message)s<', level=logging.INFO)

# function zone
def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = messages.start_message)
    return

def help_message(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = messages.help_message)
    return

def hireme_message(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = messages.hireme_message)
    userstats = [
            update.effective_user.id,
            update.effective_user.username,
            update.effective_user.language_code
            ]
    writedata(userstats)
    return

def writedata(userstats: list):
    """
    This should store a collection of userstats persistently and add new as it's called
    Then when list reaches 100 elements, it's written in csv file and emptied
    """
    if 'datasum' not in locals():
        datasum = []
    datasum.append(userstats)
    if len(datasum) >=100:
        with open(filebase.HIREME_FILENAME, 'a') as hireme_file:
            hireme_writer = csv.writer(hireme_file)
            hireme_writer.writerows(datasum)
    yield 0
#handler zone
start_handler = CommandHandler('start', start)

#disp.add_handler zone
disp.add_handler(start_handler)

#start polling
upd.start_polling()

