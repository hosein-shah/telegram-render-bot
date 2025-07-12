import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("سلام! ربات شما هم‌اکنون فعال است 🚀")

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("❌ ارور: BOT_TOKEN تنظیم نشده!")
        return

    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
