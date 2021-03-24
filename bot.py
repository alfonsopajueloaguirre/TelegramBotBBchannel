import logging
import os
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction, KeyboardButton


#Configurar logging
logging.basicConfig(
    level= logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger = logging.getLogger()

#Bloque de comandos
def start_command_handler(update, context):
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")

    update.message.reply_text(
        text='¡Hola, patetico humano!\n¿Necesitas ayuda? Usa /help',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Sobre el autor', url='https://twitter.com/AlfonsoA7X')],
        ])
    )


def help_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado la lista de comandos")
    update.message.reply_text(
        text='Estos son los comandos disponibles.\n\n/UNO - como que UNO?\n/mimir - a la cama',
    )


def uno_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado la imagen UNO")
    update.message.chat.send_photo(
        photo=open('UNO.jpeg', 'rb')
    )


def mimir_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado el gif de saber")
    update.message.chat.send_animation(
        animation=open('mimir.mp4', 'rb')
    )


#Configuracion de error
def error(update, context):
    print(f"Update{update} caused error {context.error}")


#Bloque de main
if __name__ == '__main__':

    updater = Updater(token='1791382674:AAFZ9l1jxH-wHXpFeapw5zDJ4ZelTB9XEV8', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command_handler))
    dp.add_handler(CommandHandler('UNO', uno_command_handler))
    dp.add_handler(CommandHandler('mimir', mimir_command_handler))
    dp.add_handler(CommandHandler('help', help_command_handler))

    dp.add_error_handler(error)

    updater.start_polling()
    print("BOT_CARGADO")

    updater.idle()
