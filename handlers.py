from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello! My name is EchoBot. I will echo everything you say to me."
    )

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Help!")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

