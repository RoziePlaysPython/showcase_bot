#/usr/bin/python3
from dataclasses import dataclass
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
from dumpsters import CSVDumpster


BOT_TOKEN = argv[1]
upd = Updater(token=BOT_TOKEN, use_context=True)
upd.bot.data['dumpster'] = CSVDumpster(filename = filebase.HIREME_FILENAME)
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
    context.bot.data['dumpster'].writedata(userstats)
    return

            

#handler zone
start_handler = CommandHandler('start', start)

#disp.add_handler zone
disp.add_handler(start_handler)

#start polling
upd.start_polling()

