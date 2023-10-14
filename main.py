from telebot import *
from keyboards import *

bot = TeleBot('6666010835:AAGG7yhkJis2P0KVl3k72lXx5jMl6UMKi2M')

language="ru"

with open("localizations/"+language+".json",encoding="UTF-8") as file:
    text = json.load(file)

def path(message:types.Message):
    bot.send_message(message.chat.id, 'Horray!')


def near_places(message):
    murkup = create_menu_places_keyboard()
    bot.send_message(message.chat.id, text["other"]["category"], reply_markup=murkup)


def near_performance(message):
    bot.send_message(message.chat.id, 'Horray!!!!!')


def restaurants(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, text["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v3"], reply_markup=markup)


def hotel(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, text["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)


def museam(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, text["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)


def sites(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, text["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)


def exhibition(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, text["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)


def performance(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, text["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, text["other"]["v2"], reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    markup = create_start_keyboard()
    bot.send_message(message.chat.id,
                     text["other"]["start_text"],
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text["other"]["Contact"]+'+7 950 891-51-26')


d = {"search": path,
     "round_place": near_places,
     "round_performance": near_performance,
     "restaurants": restaurants,
     "hotel": hotel,
     "museam": museam,
     "sites": sites,
     "exhibition": exhibition,
     "performance": performance}


@bot.callback_query_handler(func=lambda callback: True)
def callbacks(call):
    d[call.data](call.message)


bot.polling(none_stop=True)
