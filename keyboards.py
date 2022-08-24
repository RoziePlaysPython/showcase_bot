from telegram import InlineKeyboardButton, InlineKeyboardMarkup
hireme_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Leave Message', callback_data='lvmsg')],
        ]
    )