# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API

import telegram
from credentials import ChingDim

bot = telegram.Bot(token=ChingDim.token)
print(bot.get_me())