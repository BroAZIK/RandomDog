from flask import Flask, request
from telegram import Bot

TOKEN = "6397463095:AAGtjW-uI_QbugtFN6NHt6TG2eQ_Zwlvljc"

app = Flask(__name__)
bot = Bot(token=TOKEN)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return 'Hello, World!'

    elif request.method == 'POST':
        update = request.get_json()
        chat_id = update['message']['chat']['id']
        text = 'Assalomu alaykum!'

        bot.send_message(chat_id=chat_id, text=text)

        return 'Got a POST request!' 