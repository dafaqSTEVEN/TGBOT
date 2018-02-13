# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API

from telegram.ext import CommandHandler, Updater

from credentials import ChingDim

updater = Updater(token=ChingDim.token)
dispatcher = updater.dispatcher


def yo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('yo', yo)
dispatcher.add_handler(start_handler)

updater.start_polling()