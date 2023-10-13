import telebot
from telebot import types
import json

bot = telebot.TeleBot("6369952008:AAE14OfYmyw84nve2ndl0JCE7dww40LLCn0")
a="ru"
with open("localizations/"a+".json",encoding="UTF-8") as file:
    text = json.load(file)
    
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text["1"])
    bot.send_message(message.chat.id, text["2"])
    bot.send_message(message.chat.id, text["3"])
bot.polling(non_stop=True)