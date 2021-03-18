from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def start(update, context):

    update.message.reply_text('¡Hola, patetico humano!')

def boton(update, context):

    button1 = InlineKeyboardButton(
        text='Sobre el autor',
        url='https://twitter.com/AlfonsoA7X'
    )

    button2 = InlineKeyboardButton(
        text='Mi socio',
        url='http://mikuserver.pablofergus.com/'
    )

    button3 = InlineKeyboardButton(
        text = 'Mis comandos',
        callback_data='comandos'
    )

    update.message.reply_text(
        text='Haz click en un botón.',
        reply_markup=InlineKeyboardMarkup([
           [button1, button2, button3]
        ])
    )

def input_text(update, context):

    text = update.message.reply_text

    print(text)

def comandos_command_handler(update, context):


def comandos_callback_handler(update, context):
    query = update.callback_query
    query.answer()

    query


if __name__ == '__main__':

    updater = Updater(token='1791382674:AAFZ9l1jxH-wHXpFeapw5zDJ4ZelTB9XEV8', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('boton', boton))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('comandos', comandos_command_handler),
            CallbackQueryHandler(pattern='comandos', callback=socio_callback_handler)
        ],

        states={
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallback=[]
    ))

    updater.start_polling()
    updater.idle()
