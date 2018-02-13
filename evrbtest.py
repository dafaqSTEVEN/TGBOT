# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API

from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

from credentials import ChingDim

# Declaring a bot as a bot
updater = Updater(token=ChingDim.token)
dispatcher = updater.dispatcher


# Declaring event handlers
def yo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Echoed " + update.message.text)


# Injecting handlers
start_handler = CommandHandler('yo', yo)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

# Runs bot
updater.start_polling()
