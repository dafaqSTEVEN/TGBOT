from telegram.ext import Updater,MessageHandler,CommandHandler,RegexHandler


def grat(bot,update):
    update.message.reply_text('祝賀世界杯冠軍法國')

def rusia(bot,update):
    bot.send_photo(chat_id=-1001362330463,photo=open('C:\RUSIA.png','rb'))


def start(bot,update):
    if update.message.from_user.id==436384576:
        update.message.reply_text('屌你')
    else:
        update.message.reply_text('你都唔係大和')

def fuck(bot,update):
    update.message.reply_text('上水食雞啊　@inuwazz @kathyyyyyl @hundredyearsofchoke @jojo_jojojo')

def fucker(bot,update):
    update.message.reply_text('咁爛口架你')

def juk(bot,update):
    if update.message.from_user.id==176664889:
        update.message.reply_text('收皮啦屌你')

def tag(bot,update):
    update.message.reply_text('上水食雞啊　＠kathyyyyyl @hundredyearsofchoke @jojo_jojojo')


def main():
    updater = Updater('481320814:AAF4n6Nm4iq7oq63bSsHErVq8X-UKFt78lo')
    test = updater.dispatcher
    test.add_handler(CommandHandler('Russianboi', rusia))
    test.add_handler(CommandHandler('grat', grat))
    test.add_handler(CommandHandler('start', start))
    test.add_handler(CommandHandler('fuck', fuck))
    test.add_handler(RegexHandler('.*屌.*', fucker))
    test.add_handler(RegexHandler('.*', juk))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()