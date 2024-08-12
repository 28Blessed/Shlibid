from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

app = Flask(__name__)
TOKEN = '7225797323:AAGBWVjbbONFvWhlc5fQOWpVh6NXUEIjrpg'
bot = Bot(token=TOKEN)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    dispatcher.process_update(update)
    return "OK"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I am your game bot!")

if __name__ == '__main__':
    from telegram.ext import Dispatcher
    dispatcher = Dispatcher(bot, None, use_context=True)
    dispatcher.add_handler(CommandHandler("start", start))
    app.run(host='0.0.0.0', port=8443)
