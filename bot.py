from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import re
import sqls
import numpy.random as npr

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

f = open("scripts.sql", "r")
sqls.init_db(f.read())
f.close()


# Handle messages
def handle_message(bot, update):
    chat_id = update.message.chat_id
    mes_id = update.message.message_id
    text = update.message.text
    # WitcherShit
    if re.search(r'([Ww]itcher)+|([Вв]едьмак)+', text):
        if npr.randint(100) > 50:
            if not sqls.witchershit_check_on_delay(chat_id):
                bot.send_message(chat_id=chat_id,
                                 text=npr.choice(withcershit_texts),
                                 reply_to_message_id=mes_id)
                sqls.witchershit_update(chat_id)
    # Nintendo
    if re.search(r'([Ss]witch)+|([Сс]ви(т)?ч)+|([Nn]intendo)+|([Нн]интендо)+', text):
        if npr.randint(100) > 50:
            if not sqls.nintendo_check_on_delay(chat_id):
                bot.send_message(chat_id=chat_id,
                                 text=npr.choice(nintendo_texts),
                                 reply_to_message_id=mes_id)
                sqls.nintendo_update(chat_id)


# Handle commands
def handle_status_command(bot, update):
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    sqls.alive_update(user_id)
    if not sqls.alive_check_hate_you(user_id):
        bot.send_message(chat_id=chat_id, text=npr.choice(alive_pissed_off_texts))


def handle_audio_command(bot, update):
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='audio')


# Telegram API init
TOKEN = '982144609:AAHK3JxSpQ5BjFLCC_1mpWyPieNixFhB3QQ'
# REQUEST_KWARGS = {
#     'proxy_url': 'socks5://127.0.0.1:9051'
# }

updater = Updater(token=TOKEN)  # request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

statusCommandHandler = CommandHandler('status', handle_status_command)
audioCommandHandler = CommandHandler('audio', handle_audio_command)
messageHandler = MessageHandler(Filters.text, handle_message)

dispatcher.add_handler(statusCommandHandler)
dispatcher.add_handler(audioCommandHandler)
dispatcher.add_handler(messageHandler)

updater.start_polling(clean=True)
updater.idle()
