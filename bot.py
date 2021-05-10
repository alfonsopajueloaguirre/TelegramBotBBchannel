import logging
import os
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ChatAction, KeyboardButton, Bot
from telegram.files import sticker

#Configurar logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s."
)
logger = logging.getLogger()

#Bloque de comandos
def start_command_handler(update, context):
    logger.info(f"El usuario {update.effective_user['username']}, ha saludado al bot")

    update.message.reply_text(
        text='¡Hola, patético humano!\n¿Necesitas ayuda? Usa /help',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Sobre el autor', url='https://twitter.com/AlfonsoA7X')],
        ])
    )


def help_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado la lista de comandos")
    update.message.reply_text(
        text='Estos son los comandos disponibles:\n\n/UNO - ¿Cómo que UNO?\n/mimir - a la cama\n'
             '/lasemilla - invoca a Jose\n/27 - el número mágico\n/amigos - ver códigos de amigos\n/teparto - revienta un otaku culiao\n'
             '/arcueid - la mejor\n/bustercito - silenciar a los quickistas'
    )


def uno_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado la imagen UNO")
    update.message.chat.send_photo(
        photo=open('UNO.jpeg', 'rb')
    )


def mimir_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado mimir con Saber")
    update.message.chat.send_photo(
        photo=open('mimir.png', 'rb')
    )


def semilla_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado la imagen de la semilla")
    update.message.chat.send_photo(
        photo=open('semilla.jpg', 'rb')
    )


def te_parto_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado la imagen parte otakus")
    update.message.chat.send_photo(
        photo=open('teparto.jpg', 'rb')
    )


def amigos_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha solicitado la lista de amigos")
    update.message.reply_text(
        text='Códigos de amigo\n\nNA\nMadara: 020349652\nSócrates: 250095682\nLoreneas: 647824428\nSKIBOU: 859216994\n'
             'Pochaco: 673107507\nLopeta: 740711472\nSerjunpe: 762791833\nPendrat: 088828445\n'
             'Jaggles: 005172928\nVicky: 244515342\nSpaiky: 849736116\nNyazan: 202226679\n\nJP\nAlf: 042474419\nKatsumi: 464519697'
    )

def numero_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha invocado el número magico")
    update.message.chat.send_sticker(
        sticker='CAACAgQAAxkBAAM7YGOrTmm_xGNJA0hhCXH5-ilsE0oAAqgBAAIghU0O5euI3ERF0YceBA'
    )

def arcueid_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha nombrado a la entidad suprema")
    update.message.chat.send_photo(
        photo=open('arcueid.jpg', 'rb')
    )  

def buster_command_handler(update, context):
    user_id = update.effective_user['username']
    logger.info(f"El usuario {user_id}, ha reverenciado el meta de buster")
    update.message.chat.send_photo(
        photo=open('buster.jpg', 'rb')
    )

def sticker_id(update, context):
    print(update.message.sticker)


#Configuracion de error
def error(update, context):
    print(f"La update: {update} ha causado el error: {context.error}")


#Bloque de main token original:1791382674:AAE9O8of6GndXK06IxNnfKI6KN9S9P2S51I token prueba:1788135825:AAGK8O5i7bPxyFyOoKyC-rAyGHyMFc8Q3Hk
if __name__ == '__main__':

#Bot_BB = Bot("1791382674:AAFZ9l1jxH-wHXpFeapw5zDJ4ZelTB9XEV8")

    updater = Updater(token='1791382674:AAE9O8of6GndXK06IxNnfKI6KN9S9P2S51I', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command_handler))
    dp.add_handler(CommandHandler('UNO', uno_command_handler))
    dp.add_handler(CommandHandler('mimir', mimir_command_handler))
    dp.add_handler(CommandHandler('help', help_command_handler))
    dp.add_handler(CommandHandler('lasemilla', semilla_command_handler))
    dp.add_handler(CommandHandler('amigos', amigos_command_handler))
    dp.add_handler(CommandHandler('teparto', te_parto_command_handler))
    dp.add_handler(CommandHandler('27', numero_command_handler))
    dp.add_handler(CommandHandler('arcueid', arcueid_command_handler))
    dp.add_handler(CommandHandler('bustercito', buster_command_handler))
    dp.add_handler(MessageHandler(Filters.sticker, sticker_id))

    dp.add_error_handler(error)

    updater.start_polling()
    print("BOT_LISTO")

    updater.idle()
