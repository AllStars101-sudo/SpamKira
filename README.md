# SpamKira

This is Spam Kira. A very powerful bot for filtering messages in Telegram. It uses the Naive-Bayes algorithm for spam checking and Google Cloud AI for NSFW filtering.
<br><br>
Written in pure Python, powered by the Telegram Bot API and ```telegram-bot-python``` library.
<br><br>
It is publicly available at: https://t.me/spamkira_bot

![tumblr_6a51083fd3fdb953e16510a9b08b808e_d695871f_500](https://user-images.githubusercontent.com/53670363/128980223-09ed0d85-3122-4d66-8980-aee53426d122.gif)

# Setup and run
- Clone this repo
- Create a new Telegram bot using BotFather: https://t.me/botfather
- Run ```requirements.txt```
- Make sure to create a ```Constants.py``` file and type in your bot API key as: API_KEY = 'ENTER_YOUR_TELEGRAM_BOT_API_KEY_HERE'
- Don't forget to enable the Cloud Vision API and Cloud Video Intelligence API on Google Cloud. Create a service account too, and add in your service keys (in JSON) to the root directory of SpamKira as ```cloudcreds.json```.
- Profit!

# Motivation
There are a LOT of unnecessary spam messages that are sent on Telegram groups. I believe that this bot can defend most of them with ease.<br>
Bot theme inspired from the anime, Death Note.
