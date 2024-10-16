import telebot
import os
from dotenv import load_dotenv
import requests

load_dotenv()
token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def hello(msg):
    response = 'Привет, я помогу тебе создать диаграмму по твоему описанию!'
    bot.send_message(msg.chat.id, response)

@bot.message_handler(commands = ['help', 'помоги'])
def help(msg):
    response = 'Отправь мне описание диаграммы и Я сделаю её для тебя!'
    bot.send_message(msg.chat.id, response)


@bot.message_handler()
def get_er(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    params = {'msg': msg.text}
    response = requests.get(os.environ.get('URL'), params=params).json()
    bot.send_message(msg.chat.id, response['msg'])


bot.infinity_polling()

