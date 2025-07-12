from telegram.ext import Updater, CommandHandler

# توکن خودت رو اینجا بذار
TOKEN = '7928908717:AAGakfXJtrMTe30fRaV-a2UIHyFgSV4_5Sw'

def start(update, context):
    update.message.reply_text("سلام! به ربات من خوش اومدی 😊")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
