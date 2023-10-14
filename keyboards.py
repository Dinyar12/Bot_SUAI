from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_start_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Выбрать место и маршрут', callback_data='search')
    btn2 = InlineKeyboardButton('Показать ближайшие места', callback_data='round_place')
    btn3 = InlineKeyboardButton('Экскурсии', callback_data='round_performance')
    markup.row(btn1, btn2)
    markup.row(btn3)
    return markup


def create_menu_places_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Рестораны 🍴', callback_data='restaurants')
    btn2 = InlineKeyboardButton('Отели 🏢', callback_data='2')
    btn3 = InlineKeyboardButton('Музеи 🏛', callback_data='3')
    btn4 = InlineKeyboardButton('Выставки 🖼', callback_data='4')
    btn5 = InlineKeyboardButton('Памятники 🗿', callback_data='5')
    btn6 = InlineKeyboardButton('Мероприятия 📆', callback_data='6')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6)
    return markup
