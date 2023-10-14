from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_start_keyboard(language: dict) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(language["start_btn"]["route"], callback_data='search')
    btn2 = InlineKeyboardButton(language["start_btn"]["nearest"], callback_data='round_place')
    btn3 = InlineKeyboardButton(language["start_btn"]["excursions"], callback_data='ecscursions')
    markup.row(btn1, btn2)
    markup.row(btn3)
    return markup


def create_menu_places_keyboard(language: dict) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(language["places"]["restaurants"] + '🍴', callback_data='restaurants')
    btn2 = InlineKeyboardButton(language["places"]["hotels"] + '🏢', callback_data='hotel')
    btn3 = InlineKeyboardButton(language["places"]["museums"] + '🏛', callback_data='museam')
    btn4 = InlineKeyboardButton(language["places"]["exhibitions"] + '🖼', callback_data='exhibition')
    btn5 = InlineKeyboardButton(language["places"]["monuments"] + '🗿', callback_data='sites')
    btn6 = InlineKeyboardButton(language["places"]["events"] + '📆', callback_data='performance')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6)
    return markup


def create_information_keyboard(language: dict) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(language["information"]["info"], callback_data='info')
    btn2 = InlineKeyboardButton(language["information"]["route"], callback_data='rout')
    markup.row(btn1)
    markup.row(btn2)
    return markup
