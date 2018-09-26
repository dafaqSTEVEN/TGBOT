from telegram.ext import Updater,MessageHandler,CommandHandler,RegexHandler,filters


def grat(bot,update):
    update.message.reply_text('祝賀世界杯冠軍法國')

def rusia(bot,update):
    bot.send_photo(chat_id=-1001362330463,photo=open('C:\RUSIA.png','rb'))

def test(bot,update):
    update.message.reply_text('running normally')

def meow(bot,update):
    bot.send_video(chat_id=update.message.chat_id,video=open('E:\program\doc_2018-08-04_23-42-37.mp4', 'rb'), supports_streaming=True)

def start(bot,update):
    if update.message.from_user.id==436384576:
        update.message.reply_text('屌你')
    else:
        update.message.reply_text('你都唔係大和')

def fuck(bot,update):
    if update.message.chat_id==-1001362330463:
        update.message.reply_text('上水食雞啊　@inuwazz @kathyyyyyl @hundredyearsofchoke @jojo_jojojo')

def fucker(bot,update):
    update.message.reply_text('咁爛口架你')

def juk(bot,update):
    if update.message.from_user.id==176664889:
        update.message.reply_text('收皮啦屌你')

def countppl(bot,update):
    bot.sendMessage(update.message.chat_id, str('@' + update.message.from_user.username))

def lun(bot,update):
    update.message.reply_text('咁爛口架你')

def HTML(bot,update):
    bot.sendMessage(parse_mode='HTML',chat_id=update.message.chat_id,text='<a href="https://www.google.com">HTML running</a>')

def notsafe(bot,update):
    update.message.reply_text('懷疑入咗異空間?')

def no(bot,update):
    if update.message.from_user.id == 182025016:
        update.message.reply_text('收皮啦你')
    else:
        update.message.reply_text('182025016')

def beauty(bot,update):
    if update.message.from_user.id == 182025016:
        update.message.reply_text('收皮啦你')
    else:
        update.message.reply_text('182025016')

def lmy(bot,update):
    update.message.reply_text('啪噠！呼~呼~')

def pata(bot,update):
    update.message.reply_text('啪噠！呼~呼~')

def skin(bot,update):
    if update.message.from_user.id==436384576:
        update.message.reply_text('好的')

def balls(bot,update):
    update.message.reply_text('波你老母!')

def ball(bot,update):
    if update.message.stickers(file_id='CAADBQADsAADdwRbAZpAFC_0bw03Ag'):
        bot.sendMessage('true')


def main():
    updater = Updater('481320814:AAF4n6Nm4iq7oq63bSsHErVq8X-UKFt78lo')
    test = updater.dispatcher
    test.add_handler(CommandHandler('Russianboi', rusia))
    test.add_handler(CommandHandler('grat', grat))
    test.add_handler(CommandHandler('start', start))
    test.add_handler(CommandHandler('HTML', HTML))
    test.add_handler(CommandHandler('pata', pata))
    test.add_handler(CommandHandler('test', test))
    test.add_handler(CommandHandler('meow', meow))
    test.add_handler(CommandHandler('fuck', countppl))
    test.add_handler(RegexHandler('.*有冇雞.*', fuck))
    test.add_handler(RegexHandler('.*啪噠.*', lmy))
    test.add_handler(RegexHandler('.*美貌.*', beauty))
    test.add_handler(RegexHandler('.*不安.*', notsafe))
    test.add_handler(RegexHandler('.*撚.*', fucker))
    test.add_handler(RegexHandler('.*屌.*', fucker))
    test.add_handler(RegexHandler('.*收皮.*', skin))
    test.add_handler(RegexHandler('.*波波.*', balls))
    test.add_handler(RegexHandler('.*.*', ball))



    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()