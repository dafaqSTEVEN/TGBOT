from telegram.ext import Updater,MessageHandler,CommandHandler,RegexHandler
def main():
    updater=Updater('481320814:AAGBHPTOjI_0WumdUYqLopTJdATACL0ruC4')
    test=updater.dispatcher
    test.add_handler(CommandHandler('start',start))
    test.add_handler(CommandHandler('fuck',fuck))
    test.add_handler(RegexHandler('.*fuck.*',fucker))
    test.add_handler(RegexHandler('.*',juk))
    test.add_handler(CommandHandler('on',on))
    test.add_handler(CommandHandler('off',off))
    test.add_handler(CommandHandler('count',count))
    updater.start_polling()
    updater.idle()

X = True
Y = 0

def start(bot,update):
    if update.message.from_user.id==436384576:
        update.message.reply_text('屌你')
    else:
        update.message.reply_text('你都唔係大和!')

def fuck(bot,update):
    update.message.reply_text('你想屌大和Bot？')

def fucker(bot,update):
    update.message.reply_text('咁爛口架你')

def juk(bot,update):
    if update.message.from_user.id==436384577:
        update.message.reply_text('收皮啦屌你')

def on(bot,update):
    update.message.reply_text('開左!')
    X = True


def off(bot,update):
    X = False
    update.message.reply_text('閂左!')

def count(bot, update):
    if X ==True:
        Y += 1 and update.message.reply_text('你依加數到第',Y,'次!')


if __name__ == '__main__':
    main()
