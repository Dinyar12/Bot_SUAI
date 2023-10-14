from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_start_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Выбрать место и маршрут', callback_data='search')
    btn2 = InlineKeyboardButton('Показать ближайшие места', callback_data='round_place')
    btn3 = InlineKeyboardButton('Экскурсии', callback_data='ecscursions')
    markup.row(btn1, btn2)
    markup.row(btn3)
    return markup


def create_menu_places_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Рестораны 🍴', callback_data='restaurants')
    btn2 = InlineKeyboardButton('Отели 🏢', callback_data='hotel')
    btn3 = InlineKeyboardButton('Музеи 🏛', callback_data='museam')
    btn4 = InlineKeyboardButton('Выставки 🖼', callback_data='exhibition')
    btn5 = InlineKeyboardButton('Памятники 🗿', callback_data='sites')
    btn6 = InlineKeyboardButton('Мероприятия 📆', callback_data='performance')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6)
    return markup


def create_information_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Информация', callback_data='info')
    btn2 = InlineKeyboardButton('Проложить маршрут', callback_data='rout')
    markup.row(btn1)
    markup.row(btn2)
    return markup
