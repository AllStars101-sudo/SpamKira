import Constants as keys
from telegram.ext import *
import Responses as R
import os
import SpamDetector as spam
import VideoScanner as vidscan

print("Bot started")

def start_command(update, context):
    update.message.reply_text("Hi, I'm Kira. I hate spam and I write your name in my Death Note if you spam any of the groups I'm in. MwahahahahahahhaHAHAHAHAHAHAAHA")
    update.message.reply_video(video=open('start.mp4', 'rb'), supports_streaming=True)

def help_command(update, context):
    update.message.reply_text("Yeah, you don't deserve help. Also,")
    update.message.reply_video(video=open('chip.mp4', 'rb'), supports_streaming=True)


def handle_message(update, context):
    if update.message.photo:
        file = update.message.photo[-1].get_file()
        path = file.download("output.jpg")
        if R.detect_safe_search(path) in ["racy: VERY_LIKELY", "racy: LIKELY"]:
            response=str(update.message.from_user)+"has been kicked."
            os.remove(path)
            update.message.reply_text(response)
            update.message.delete()
        elif R.detect_safe_search(path) in ["racy: POSSIBLE"]:
            os.remove(path)
            update.message.reply_text("I can't determine exactly if this is NSFW or not (it is possible) so I'm not going to write your name in my Death Note.")
        else:
            os.remove(path)
    elif update.message.text:
        if str(update.message.text) in ["free","tf", "trading", "video", "send some video", "porn"]:
            pass
        elif spam.predict_spam(str(update.message.text)):
            result = ["This is spam. I've written your name in my Death Note.","Ohhh, this is a normal message."]
            update.message.reply_text(result[0])
    elif update.message.video:
        file = update.message.video.get_file()
        path = file.download("output.mp4")
        if vidscan.videoscanner(path) in ["pornogaphy: VERY_LIKELY", "pornogaphy: LIKELY"]:
            response=str(update.message.from_user)+"has been kicked."
            os.remove(path)
            update.message.reply_text(response)
            update.message.delete()
        elif vidscan.videoscanner(path) in ["pornogaphy: POSSIBLE"]:
            os.remove(path)
            update.message.reply_text("I can't determine exactly if this is NSFW or not (it is possible) so I'm not going to write your name in my Death Note.")
        else:
            os.remove(path)
            update.message.reply_text("nice video")
    elif update.message.document.mime_type == "video/mp4":
        file = update.message.document.get_file()
        path = file.download("output.mp4")
        if vidscan.videoscanner(path) in ["pornogaphy: VERY_LIKELY", "pornogaphy: LIKELY"]:
            response=str(update.message.from_user)+"has been kicked."
            os.remove(path)
            update.message.reply_text(response)
            update.message.reply_video(video=open('nonsfw.mp4', 'rb'), supports_streaming=True)
            update.message.delete()
        elif vidscan.videoscanner(path) in ["pornogaphy: POSSIBLE"]:
            os.remove(path)
            update.message.reply_text("I can't determine exactly if this is NSFW or not (it is possible) so I'm not going to write your name in my Death Note.")
        else:
            os.remove(path)
    

def error(update, context):
    print(f"Update {update} caused error{context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    photo_handler = MessageHandler(Filters.photo, handle_message)
    dp.add_handler(photo_handler)
    video_handler = MessageHandler(Filters.video, handle_message)
    dp.add_handler(video_handler)
    gif_handler = MessageHandler(Filters.document, handle_message)
    dp.add_handler(gif_handler)
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()