import os
import re
import sys
import numpy.random as npr
from telegram.ext import Updater, MessageHandler, PrefixHandler, Filters
import sqls

sticker_mode_chat_ids = set()
reminder_jobs = dict()

witchershit_text = 'Ведьмак говно'
witchershit_reminder_texts = ['Держу вас в тонусе', 'Просто напоминаю', 'Кто, если не я?']

# Инициализация таблиц в БД
sqls.init_db()

# Вывод принтов в лог-файл, если не под PyCharm
if not os.environ.get('PYTHONUNBUFFERED'):
    sys.stdout = open("log.txt", "w")
    sys.stderr = open("err.txt", "w")

# Telegram API init
ft = open("witchershit_bot.token", "r")
# ft = open("witchershit_test_bot.token", "r")
TOKEN = ft.read()
ft.close()

# REQUEST_KWARGS = {
#     'proxy_url': 'socks5://127.0.0.1:9150'
# }

updater = Updater(token=TOKEN, use_context=True)  # , request_kwargs=REQUEST_KWARGS)
job_queue = updater.job_queue
dispatcher = updater.dispatcher


def callback_witchershit_reminder(context):
    chat_id = context.job.context
    context.bot.send_message(chat_id=chat_id, text=witchershit_text)
    context.bot.send_message(chat_id=chat_id, text=npr.choice(witchershit_reminder_texts))
    sqls.witchershit_update(chat_id)
    global reminder_jobs
    try:
        del reminder_jobs[chat_id]
        context.bot.send_message(chat_id=149352641, text=str(chat_id) + ': reminder succeeded')
    except KeyError:
        pass


# Handle messages
def handle_message(update, context):
    bot = context.bot
    chat_id = update.message.chat_id
    mes_id = update.message.message_id
    text = update.message.text
    # Sticker mode
    global sticker_mode_chat_ids
    if chat_id in sticker_mode_chat_ids:
        bot.send_message(chat_id=chat_id, text='Wrong sticker. Abort')
        sticker_mode_chat_ids.discard(chat_id)
    # WitcherShit
    if re.search(r'(?i)(witcher|ведьмак)+', text):
        if re.search(r'(?i)ведьмак([\s\-—]){1,3}(г[ао]вно)$', text):
            bot.send_message(chat_id=chat_id,
                             text='+',
                             reply_to_message_id=mes_id)
        elif not sqls.witchershit_check(chat_id):
            bot.send_message(chat_id=chat_id,
                             text=witchershit_text,
                             reply_to_message_id=mes_id)
            sqls.witchershit_update(chat_id)
    # WitcherShit Reminder
    global reminder_jobs
    try:
        job = reminder_jobs[chat_id]
        job.schedule_removal()
        del reminder_jobs[chat_id]
        bot.send_message(chat_id=149352641, text=str(chat_id) + ': reminder deleted')
    except KeyError:
        pass
    if not sqls.witchershit_check(chat_id):
        if npr.randint(100) > 80:
            delay = 3600 + npr.randint(32400) + 3600  # 1 час + от 0 до 9 часов
            # delay = 5 + npr.randint(10)
            info = str(chat_id) + ': reminder set for ' + str(delay) + ' sec, ' + str(update.message.chat.title)
            bot.send_message(chat_id=149352641, text=info)
            reminder_jobs[chat_id] = job_queue.run_once(callback_witchershit_reminder, delay, context=chat_id)
    # Nintendo
    if re.search(r'(?i)(switch|сви(т)?ч|nintendo|нинтендо)+', text):
        if not sqls.nintendo_check(chat_id):
            phrase = sqls.nintendo_get_phrase_update(chat_id)
            if phrase:
                bot.send_message(chat_id=chat_id,
                                 text=phrase,
                                 reply_to_message_id=mes_id)
    # Beutiful
    if re.search(r'(?i)(красиво([.!])?)$', text):
        if not sqls.beautiful_check_on_delay(chat_id):
            bot.send_sticker(chat_id=chat_id,
                             sticker='CAADAgADHAUAAnKq5gTUAstCxSdgJhYE')
            sqls.beautiful_update(chat_id)


# Handle sticker
def handle_sticker(update, context):
    bot = context.bot
    global sticker_mode_chat_ids
    chat_id = update.message.chat_id
    if chat_id in sticker_mode_chat_ids:
        bot.send_message(chat_id=chat_id, text=update.message.sticker.file_id)
        sticker_mode_chat_ids.discard(chat_id)


# Handle commands
def handle_status_command(update, context):
    bot = context.bot
    chat_id = update.message.chat_id
    if not sqls.status_check(chat_id):
        phrase = sqls.status_get_phrase_update(chat_id)
        if phrase:
            bot.send_message(chat_id=chat_id, text=phrase)


def handle_pingo_command(update, context):
    bot = context.bot
    # user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='pongo')


def handle_sticker_command(update, context):
    bot = context.bot
    chat_id = update.message.chat_id
    chat_type = update.message.chat.type
    if chat_type == 'private':
        global sticker_mode_chat_ids
        sticker_mode_chat_ids.add(chat_id)
        bot.send_message(chat_id=chat_id, text='Ready. Send me a sticker')


# Register handlers
statusPrefixHandler = PrefixHandler('/', 'status', handle_status_command)
pingoPrefixHandler = PrefixHandler('/', 'pingo', handle_pingo_command)
stickerPrefixHandler = PrefixHandler('/', 'sticker', handle_sticker_command)
stickerHandler = MessageHandler(Filters.sticker, handle_sticker)
messageHandler = MessageHandler(Filters.text, handle_message)

dispatcher.add_handler(statusPrefixHandler)
dispatcher.add_handler(pingoPrefixHandler)
dispatcher.add_handler(stickerPrefixHandler)
dispatcher.add_handler(stickerHandler)
dispatcher.add_handler(messageHandler)

# Bot start
updater.start_polling(clean=True)
updater.idle()
