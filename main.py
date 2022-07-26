#/usr/bin/python3
from sys import argv
from telegram import Bot
from telegram.ext import (
    Filters,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler as CQHandler,
    ConversationHandler,
    Updater
)
import logging
logging.basicConfig(format='>%(asctime)s - %(name)s - %(levelname)s - %(message)s<', level=logging.INFO)

import messages # message text
import filebase # filenames for persistence and other stuff
import keyboards # Keyboard objects
from dumpsters import CSVDumpster

BOT_TOKEN = argv[1]
CREATOR_ID = int(argv[2])
DEFAULT_LANG = 'en'
bot = Bot(token=BOT_TOKEN)
upd = Updater(bot=bot, use_context=True)
disp = upd.dispatcher
disp.bot_data['dumpster'] = CSVDumpster(filename = filebase.HIREME_FILENAME)
disp.bot_data['creator'] = CREATOR_ID

# function zone
def check_lang(update, context):
    if 'lang' not in context.user_data.keys():
        context.user_data['lang'] = DEFAULT_LANG
    return context.user_data['lang']

def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, 
        text = messages.start_message_text,
        reply_markup = keyboards.lang_keyboard)
    return

def lang_callback(update, context):
    query = update.callback_query
    print(query.data)
    lang = query.data if query.data in messages.LANG_SUPPORT else 'en' # this should prevent forging callback data
    context.user_data['lang'] = lang
    query.answer(text = messages.lang_callback_text[lang])

def help_message(update, context):
    lang = check_lang(update, context)
    context.bot.send_message(chat_id = update.effective_chat.id, 
        text = messages.help_message_text[lang],
        parse_mode = 'MarkdownV2'
        )
    return

def hireme_message(update, context):
    lang = check_lang(update, context)
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = messages.hireme_message_text[lang],
        reply_markup = keyboards.hireme_keyboard,
        parse_mode = 'MarkdownV2'
        )
    userstats = (
        update.effective_user.id,
        update.effective_user.username,
        update.effective_user.language_code
        )
    context.bot_data['dumpster'].writedata(userstats)
    return 0

def hireme_callback(update, context):
    lang = check_lang(update, context)
    query = update.callback_query
    query.answer(text = messages.hireme_callback_answer_message_text[lang], )
    context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = messages.hireme_callback_answer_message_text[lang],
        )
    return 1

def leave_message(update, context):
    lang = check_lang(update, context)
    context.bot.send_message(
        chat_id = context.bot_data['creator'],
        text = f"{update.effective_user.name} wants to contact you. Here's their message: \n{update.message.text}"
        )
    update.message.reply_text('Your message has been received')
    return ConversationHandler.END

def cancel_message(update, context):
    lang = check_lang(update, context)
    update.message.reply_text(messages.cancel_message_text[lang])
    return ConversationHandler.END

def sort_init(update, context):
    lang = check_lang(update, context)
    update.message.reply_text(messages.sort_message_text[lang])
    return 1

def sort_continue(update, context):
    lang = check_lang(update, context)
    arr = list(map(int, update.message.text.split(' ')))
    sorted_arr = merge_sort(arr)
    update.message.reply_text(', '.join(map(str, sorted_arr)))
    update.message.reply_text(messages.sort_continue_message_text[lang])
    return 1

def merge_sort(alist: list) -> list:
    def merge(lista: list, listb: list) -> list:
        idxa, idxb = 0, 0
        result = []
        while idxa < len(lista) and idxb < len(listb):
            result.append(min(lista[idxa], listb[idxb]))
            if lista[idxa] >= listb[idxb]:
                idxb+=1
            else:
                idxa+=1
        return result+lista[idxa:]+listb[idxb:]
    def split(alist: list) -> list:
        if len(alist)<=1:
            return alist
        half = len(alist)//2
        return merge(split(alist[:half]), split(alist[half:]))
    sortedlist = split(alist)
    return sortedlist

def blur_init(update, context):
    lang = check_lang(update, context)
    update.message.reply_text(messages.blur_init_message_text[lang])
    return 0

# TODO: implement a way to download file via its id
# TODO: implement gaussian blur functionality
def blur_continue(update, context):
    lang = check_lang(update, context)
    print([photo.file_id for photo in update.message.photo])
    return ConversationHandler.END

#handler zone
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help_message)
cancel_message_handler = CommandHandler('cancel', callback=cancel_message)
lang_handler = CQHandler(lang_callback, pattern = r'(en|ru)')

hireme_conv_handler = ConversationHandler(
    entry_points = [CommandHandler('hireme', hireme_message), CQHandler(hireme_callback, pattern = 'lvmsg')],
    states = {
        0: [CQHandler(hireme_callback, pattern = 'lvmsg')],
        1: [MessageHandler(~Filters.command, leave_message)],
    },
    fallbacks = [cancel_message_handler],
)

sort_conv_handler = ConversationHandler(
    entry_points = [CommandHandler('sort', sort_init)],
    states = {
        1: [MessageHandler(Filters.regex(r'[0-9, ,-].*'), sort_continue)],
    },
    fallbacks = [cancel_message_handler],
)

blur_conv_handler = ConversationHandler(
    entry_points = [CommandHandler('blur', blur_init)],
    states = {
        0: [MessageHandler(Filters.photo, blur_continue)],
        },
    fallbacks = [cancel_message_handler],
)

#disp.add_handler zone
disp.add_handler(start_handler)
disp.add_handler(help_handler)
disp.add_handler(hireme_conv_handler)
disp.add_handler(sort_conv_handler)
disp.add_handler(blur_conv_handler)
disp.add_handler(lang_handler)

#start polling
upd.start_polling()
