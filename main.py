from telebot import *

import test
from keyboards import *
from test import *

bot = TeleBot('6666010835:AAGG7yhkJis2P0KVl3k72lXx5jMl6UMKi2M')


def path(message):
    bot.send_message(message.chat.id, 'Введите адрес места, куда хотите попасть:')
    bot.register_next_step_handler(message, card)


def near_places(message):
    murkup = create_menu_places_keyboard()
    bot.send_message(message.chat.id, 'Выберите категорию мест, которую Вы хотите посетить', reply_markup=murkup)


def ecscursions(message):
    bot.send_message(message.chat.id, 'Horray!!!!!')


def restaurants(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, 'Вариант1:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант2:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант3:', reply_markup=markup)


def hotel(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, 'Вариант1:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант2:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант3:', reply_markup=markup)


def museam(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, 'Вариант1:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант2:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант3:', reply_markup=markup)


def sites(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, 'Вариант1:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант2:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант3:', reply_markup=markup)


def exhibition(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, 'Вариант1:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант2:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант3:', reply_markup=markup)


def performance(message):
    markup = create_information_keyboard()
    bot.send_message(message.chat.id, 'Вариант1:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант2:', reply_markup=markup)
    bot.send_message(message.chat.id, 'Вариант3:', reply_markup=markup)


def info(message):
    bot.send_message(message.chat.id, 'Информация...')


def card(message):
    m = message.text
    API(m)
    bot.send_photo(message.chat.id, photo=test.img)


@bot.message_handler(commands=['start'])
def start(message):
    markup = create_start_keyboard()
    bot.send_message(message.chat.id,
                     'Бот может предоставлять информацию о популярных туристических направлениях, а также о местных достопримечательностях и мероприятиях. Он может также отвечать на вопросы пользователей о том, что посмотреть и чем заняться в том или ином месте.'
                     'Бот может помогать спланировать маршрут путешествия, бронированием билетов и гостиниц. Он может предлагать различные варианты маршрутов, основанные на интересах пользователя, и помогать с поиском и бронированием билетов и гостиниц по лучшим ценам.'
                     'Бот может предоставлять персонализированные рекомендации и советы пользователям. Он может также помогать с решением проблем, которые могут возникнуть во время путешествия.\n'
                     '<b>Travel Bot - это полезный инструмент для путешественников, желающих узнать больше о том или ином месте и спланировать свое путешествие.</b>',
                     reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Контакты техподдежки: +7 950 891-51-26')


d = {"search": path,
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
    d[call.data](call.message)


bot.polling(none_stop=True)
