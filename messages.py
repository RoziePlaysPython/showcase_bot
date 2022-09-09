# Only one language for start message since user haven't chosen yet
LANG_SUPPORT = ['en', 'ru']

start_message_text = '''
Hello, this is a multitool bot made to showcase my developer skills.
send /help to get list of all possible commands.
Привет, это универсальный бот, сделанный мною для портфолио.
Пиши /help для списка доступных команд
Этот бот так же доступен на русском языке (По умолчанию на английском), язык можно переключить по кнопке ниже.
'''

lang_callback_text = {
    "en": '''Language changed to english''',
    "ru": '''Язык сменён на русский'''
}

# MarkdownV2 mode (some characters have to be preceded with '\')
help_message_text ={
    "en":  '''
These are all commands I can interact with:
    /help \- this message
    /hireme \- leave a message for me and view my contact information
    /sort \- sort an array of integers using merge sort algorithm \(check this on [github](https://github.com/RoziePlaysPython/showcase_bot)\!\)
    /blur \- I will blur your pics for you
''',
    "ru": '''
Вот команды, которые я пойму:
    /help \- Это сообщение
    /hireme \- Узнать контакты автора и оставить сообщение
    /sort \- Отсортировать массивс помошью алгоритма merge sort \([github](https://github.com/RoziePlaysPython/showcase_bot)\!\)
    /blur \- Размою ваши картинки\.
'''
}

hireme_message_text ={
    "en":  '''
You can leave a message for me with a button below\.
However, if you are willing to contact me directly, here are my links:
[Telegram](https://t.me/uwuashell)
[HH резюме РУ](https://hh.ru/resume/f0876ad0ff0af6e0f30039ed1f706d4e395934)
[HH resume EN](https://hh.ru/resume/44a6c226ff0af3d4950039ed1f675230374554)
''',
    "ru": '''
Вы можете оставить сообщение для меня по кнопке ниже\.
Однако, если вы хотите связаться со мной напрямую, вот мои контакты, а также ссылки на резюме:
[Telegram](https://t.me/uwuashell)
[HH резюме РУ](https://hh.ru/resume/f0876ad0ff0af6e0f30039ed1f706d4e395934)
[HH resume EN](https://hh.ru/resume/44a6c226ff0af3d4950039ed1f675230374554)
'''
}

hireme_callback_answer_message_text ={
    "en":  '''
Send your message and this bot will notify me.
''',
    "ru": '''
Напишите своё сообщение и этот бот уведомит меня.
'''
}

cancel_message_text ={
    "en":  '''
This conversation has been cancelled.
''',
    "ru": '''
Эта ветка диалога отменена.
'''
}

sort_message_text ={
    "en":  '''
Send me an array of numbers separated by spaces.
For example:
1 23 69 -91 420
or send /cancel to cancel
''',
    "ru": '''
Отправьте мне массив чисел, разделенных пробелом.
Например:
1 23 69 -91 420
или отправьте /cancel для отмены
'''
}

sort_continue_message_text ={
    "en":  '''
Sorted in @time.
You can send another array or /cancel
''',
    "ru": '''
Время сортировки: @time
Вы можете отправить ещё один массив или /cancel
'''
}

blur_init_message_text ={
    "en":  '''
Send me a pic and I will use gaussian blur algorithm on it.
''',
    "ru": '''
Отправьте мне картинку и я применю размытие по гауссу к ней.
'''
}

