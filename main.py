from telebot import *
from keyboards import *

bot = TeleBot('6313558465:AAE5SsYQFP9N6oSZZjdar1Mne1UqnR6tXac')


def path(message:types.Message):
    bot.send_message(message.chat.id, 'Horray!')


def near_places(message):
    murkup = create_menu_places_keyboard()
    bot.send_message(message.chat.id, 'Выберите категорию мест, которую Вы хотите посетить', reply_markup=murkup)


def near_performace(message):
    bot.send_message(message.chat.id, 'Horray!!!!!')


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
    bot.send_message(message.chat.id, 'Контакты техподдежки: +7 921-1488-1488')


d = {"search": path,
     "round_place": near_places,
     "round_performance": near_performace}


@bot.callback_query_handler(func=lambda callback: True)
def callbacks(call):
    d[call.data](call.message)


bot.polling(none_stop=True)
