from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

language="ru"

with open("localizations/"+language+".json",encoding="UTF-8") as file:
    text = json.load(file)
    
def create_start_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text["start_btn"]["route"], callback_data='search')
    btn2 = InlineKeyboardButton(text["start_btn"]["nearest"], callback_data='round_place')
    btn3 = InlineKeyboardButton(text["start_btn"]["excursions"], callback_data='round_performance')
    markup.row(btn1,btn2)
    markup.row(btn3)
    return markup


def create_menu_places_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text["places"]["restaurants"]+'🍴', callback_data='restaurants')
    btn2 = InlineKeyboardButton(text["places"]["hotels"]+'🏢', callback_data='hotel')
    btn3 = InlineKeyboardButton(text["places"]["museums"]+'🏛', callback_data='museam')
    btn4 = InlineKeyboardButton(text["places"]["exhibitions"]+'🖼', callback_data='exhibition')
    btn5 = InlineKeyboardButton(text["places"]["monuments"]+'🗿', callback_data='sites')
    btn6 = InlineKeyboardButton(text["places"]["events"]+'📆', callback_data='performance')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6)
    return markup


def create_information_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text["information"]["info"], callback_data='info')
    btn2 = InlineKeyboardButton(text["information"]["route"], callback_data='rout')
    markup.row(btn1)
    markup.row(btn2)
    return markup
