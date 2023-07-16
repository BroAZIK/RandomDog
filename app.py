from flask import Flask, request

from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from handlers import start, help, echo

TOKEN = "5922381162:AAHZlv7P-uypWE8IzpQd0F6pZq9vex_IhyI"

TOKEN = os.environ.get('TOKEN')
bot = Bot(token=TOKEN)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'webhook is working!'

    elif request.method == 'POST':
        dp = Dispatcher(bot, None, workers=0)

        update = Update.de_json(request.get_json(force=True), bot)
        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        dp.add_handler(MessageHandler(Filters.text, echo))

        dp.process_update(update)

        return 'Got a POST request!'

