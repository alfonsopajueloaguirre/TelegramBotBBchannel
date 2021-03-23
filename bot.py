import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction


INPUT_TEXT_STATE = 0


def start_command_handler(update, context):

    update.message.reply_text(
        text='¡Hola, patetico humano! \n\n Usa /qr para generar un codigo qr.',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Generar QR', callback_data='qr')],
            [InlineKeyboardButton(text='Sobre el autor', url='https://twitter.com/AlfonsoA7X')],
        ])
    )


def uno_command_handler(update, context):
    update.message.chat.send_photo(
        photo=open('UNO.jpeg', 'rb')
    )


def mimir_command_handler(update, context):
    update.message.chat.send_animation(
        animation=open('mimir.mp4', 'rb')
    )


#Funcion QR
def qr_command_handler(update, context):

    update.message.reply_text('Enviame un texto para generarte un codigo QR.')

    return INPUT_TEXT_STATE


def generate_qr(text):

    filename = text + '.jpg'

    img = qrcode.make(text)
    img.save(filename)

    return filename


def input_text(update, context):
    text = update.message.text

    filename = generate_qr(text)

    chat = update.message.chat

    send_qr(filename, chat)

    return ConversationHandler.END


def send_qr(filename, chat):

    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )

    chat.send_photo(
        photo=open(filename, 'rb')
    )

    os.unlink(filename)


#Funcion QR END
def qr_callback_handler(update, context):

    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text='Enviame un texto para generarte un codigo QR.'
    )

    return INPUT_TEXT_STATE


if __name__ == '__main__':

    updater = Updater(token='1791382674:AAFZ9l1jxH-wHXpFeapw5zDJ4ZelTB9XEV8', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command_handler))
    dp.add_handler(CommandHandler('UNO', uno_command_handler))
    dp.add_handler(CommandHandler('mimir', mimir_command_handler))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', qr_command_handler),
            CallbackQueryHandler(pattern='qr', callback=qr_callback_handler)
        ],

        states={
            INPUT_TEXT_STATE: [MessageHandler(Filters.text, input_text)]
        },

        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()
