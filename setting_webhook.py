from telegram import Bot

TOKEN = "5809174742:AAFK-9p2LXXoa-OIHwYpsKO_VPKBJJ0beuc"

bot = Bot(token=TOKEN)

print(bot.set_webhook("https://echobotdeploy.pythonanywhere.com"))