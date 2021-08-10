import Constants as keys
from telegram.ext import *
import Responses as R
from io import BytesIO
import os
import time


print("Bot started")

def start_command(update, context):
    update.message.reply_text("Hi, I'm Kira. I hate spam and I write your name in a death note if you spam any of the groups I'm in. MwahahahahahahhaHAHAHAHAHAHAAHA")

def help_command(update, context):
    update.message.reply_text("Yeah, you don't deserve help.")

def handle_message(update, context):
    #file = context.bot.get_file(update.message.photo[-1].file_id)
    #f =  BytesIO(file.download_as_bytearray())

    # f is now a file object you can do something with

    #result = R.detect_safe_search(f)

    #response = 'I procsseed that and the result was %s' % (result,)

    #context.bot.send_message(chat_id=update.message.chat_id, text=response)
    #text= str(update.message.photo).lower()
    #response = R.detect_safe_search(text)
    #print(update.message.location)
    file = update.message.photo[-1].get_file()
    path = file.download("output.jpg")
    response = R.detect_safe_search(path)
    os.remove(path)
    update.message.reply_text(response)
    

def error(update, context):
    print(f"Update {update} caused error{context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    photo_handler = MessageHandler(Filters.photo, handle_message)
    dp.add_handler(photo_handler)
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()