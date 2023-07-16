from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import start, help, echo

import os

TOKEN = os.environ.get('TOKEN')

def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()