from telegram import InlineKeyboardButton, InlineKeyboardMarkup
lang_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = 'English', callback_data='en'), 
            InlineKeyboardButton(text = 'Русский', callback_data='ru')
        ]
    ]
)
hireme_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Leave Message', callback_data='lvmsg')
        ],
    ]
)
