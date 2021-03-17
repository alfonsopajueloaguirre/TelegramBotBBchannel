from telegram.ext import Updater, CommandHandler

def start(update, context):

    update.message.reply_text('Hola, humano!')


if __name__ == '__main__':

    updater = Updater(token='1791382674:AAFZ9l1jxH-wHXpFeapw5zDJ4ZelTB9XEV8', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()
