import os
import re
import sys
import numpy.random as npr
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import sqls

sticker_mode_chat_id = 0

withcershit_texts = ['Ведьмак — говно', 'Ведьмак 3 — тупая гриндилка без сюжета',
                     'Хуйня ваш Ведьмак 3. В игре слишком много мата', 'Геральт — педик']

nintendo_texts = ['Нинтендо сосёт', 'Свитч хрень, игор нет', 'А сонька круче']

alive_pissed_off_texts = ['Сука, падла', 'Где тут дрын, какой-нибудь?!',
                          'Никак вы, блять, не научитесь', 'Вот ссука',
                          'Статус, статус. Хуй те а не статус!', 'Лютик, блять!',
                          'Я тя на хер пошлю, ты меня. И чё?\nОбнимемся и вместе пойдем',
                          'С нами лучше не балуй.\nЛишь бы цел остался ...',
                          'Найдите себе другое развлечение. Не знаю, наловите лягушек, '
                          'навставляйте им в жопы соломинок',
                          'Ламберт, Ламберт, хер моржовый.\nЛамберт, Ламберт, вредный хуй.']

# Инициализация таблиц в БД
f = open("scripts.sql", "r")
sqls.init_db(f.read())
f.close()

# Вывод принтов в лог-файл, если не под PyCharm
if not os.environ.get('PYTHONUNBUFFERED'):
    sys.stdout = open("log.txt", "w")
    sys.stderr = open("err.txt", "w")


# Handle messages
def handle_message(bot, update):
    chat_id = update.message.chat_id
    mes_id = update.message.message_id
    text = update.message.text
    # Sticker mode
    global sticker_mode_chat_id
    if sticker_mode_chat_id == chat_id:
        bot.send_message(chat_id=chat_id, text='Wrong sticker. Abort')
        sticker_mode_chat_id = 0
    # WitcherShit
    if re.search(r'(?i)(witcher|ведьмак)+', text):
        if npr.randint(100) > 50:
            if not sqls.witchershit_check_on_delay(chat_id):
                bot.send_message(chat_id=chat_id,
                                 text=npr.choice(withcershit_texts),
                                 reply_to_message_id=mes_id)
                sqls.witchershit_update(chat_id)
    # Nintendo
    if re.search(r'(?i)(switch|сви(т)?ч|nintendo|нинтендо)+', text):
        if npr.randint(100) > 50:
            if not sqls.nintendo_check_on_delay(chat_id):
                bot.send_message(chat_id=chat_id,
                                 text=npr.choice(nintendo_texts),
                                 reply_to_message_id=mes_id)
                sqls.nintendo_update(chat_id)
    # Beutiful
    if re.search(r'(?i)(красиво([.!])?)$', text):
        if not sqls.beautiful_check_on_delay(chat_id):
            bot.send_sticker(chat_id=chat_id,
                             sticker='CAADAgADHAUAAnKq5gTUAstCxSdgJhYE')
            sqls.beautiful_update(chat_id)


# Handle sticker
def handle_sticker(bot, update):
    global sticker_mode_chat_id
    chat_id = update.message.chat_id
    if chat_id == sticker_mode_chat_id:
        bot.send_message(chat_id=chat_id, text=update.message.sticker.file_id)
        sticker_mode_chat_id = 0


# Handle commands
def handle_status_command(bot, update):
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    sqls.alive_update(user_id)
    if not sqls.alive_check_hate_you(user_id):
        bot.send_message(chat_id=chat_id, text=npr.choice(alive_pissed_off_texts))


def handle_pingo_command(bot, update):
    # user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='pongo')


def handle_sticker_command(bot, update):
    global sticker_mode_chat_id
    chat_id = update.message.chat_id
    chat_type = update.message.chat.type
    if chat_type == 'private':
        # print('smode', sticker_mode_chat_id, chat_id, chat_type)
        sticker_mode_chat_id = chat_id
        bot.send_message(chat_id=chat_id, text='Ready. Send me a sticker')


# Telegram API init
TOKEN = '965449851:AAF9tKfgA50Mrr8paPB4B2BicnbJ8BuPahk'
# REQUEST_KWARGS = {
#     'proxy_url': 'socks5://127.0.0.1:9051'
# }

updater = Updater(token=TOKEN, use_context=True)  # request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

statusCommandHandler = CommandHandler('status', handle_status_command)
pingoCommandHandler = CommandHandler('pingo', handle_pingo_command)
stickerCommandHandler = CommandHandler('sticker', handle_sticker_command)
stickerHandler = MessageHandler(Filters.sticker, handle_sticker)
messageHandler = MessageHandler(Filters.text, handle_message)

dispatcher.add_handler(statusCommandHandler)
dispatcher.add_handler(pingoCommandHandler)
dispatcher.add_handler(stickerCommandHandler)
dispatcher.add_handler(stickerHandler)
dispatcher.add_handler(messageHandler)

updater.start_polling(clean=True)
updater.idle()
