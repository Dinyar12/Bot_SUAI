import json

from telebot import *

import test
from keyboards import *
from test import *

settings = json.load(open("settings",encoding="UTF-8"))

languages = ["ru", "en"]
localizations = {}
current_language = settings["default_language"]

for lang in languages:
    with open("localizations/" + lang + ".json", encoding="UTF-8") as file:
        localizations[lang] = json.load(file)

bot = TeleBot(settings["token"])


def path(message: types.Message):
    bot.send_message(message.chat.id, 'Введите адрес места, куда хотите попасть:')
    bot.register_next_step_handler(message, card)


def near_places(message):
    markup = create_menu_places_keyboard(localizations[current_language])
    bot.send_message(message.chat.id, localizations[current_language]["other"]["category"], reply_markup=markup)


def ecscursions(message):
    bot.send_message(message.chat.id, 'Horray!!!!!')


def restaurants(message):
    markup = create_information_keyboard(localizations[current_language])
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v3"], reply_markup=markup)


def hotel(message):
    markup = create_information_keyboard(localizations[current_language])
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)


def museam(message):
    markup = create_information_keyboard(localizations[current_language])
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)


def sites(message):
    markup = create_information_keyboard(localizations[current_language])
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)


def exhibition(message):
    markup = create_information_keyboard(localizations[current_language])
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)


def performance(message):
    markup = create_information_keyboard(localizations[current_language])
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v1"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)
    bot.send_message(message.chat.id, localizations[current_language]["other"]["v2"], reply_markup=markup)


def info(message):
    bot.send_message(message.chat.id, 'Информация...')


def card(message):
    m = message.text
    API(m)
    bot.send_photo(message.chat.id, photo=test.img)


@bot.message_handler(commands=['start'])
def start(message):
    markup = create_start_keyboard(localizations[current_language])
    bot.send_message(message.chat.id,
                     localizations[current_language]["other"]["start_text"],
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, localizations[current_language]["other"]["Contact"] + '+7 950 891-51-26')


@bot.message_handler(commands=['language'])
def trans(message):
    global current_language
    if current_language == "ru":
        current_language = "en"
        bot.send_message(message.chat.id, 'Язык успешно изменён')
    else:
        current_language = "ru"
        bot.send_message(message.chat.id, 'Language successfully changed')


switch = {"search": path,
          "round_place": near_places,
          "ecscursions": ecscursions,
          "restaurants": restaurants,
          "hotel": hotel,
          "museam": museam,
          "sites": sites,
          "exhibition": exhibition,
          "performance": performance,
          "info": info}


@bot.callback_query_handler(func=lambda callback: True)
def callbacks(call):
    switch[call.data](call.message)


bot.polling(none_stop=True)
