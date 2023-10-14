from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

language="en"

with open("localizations/"+language+".json",encoding="UTF-8") as file:
    text = json.load(file)
    
def create_start_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text["start"]["route"], callback_data='search')
    btn2 = InlineKeyboardButton(text["start"]["nearest"], callback_data='round_place')
    btn3 = InlineKeyboardButton(text["start"]["excursions"], callback_data='round_performance')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    return markup


def create_menu_places_keyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text["places"]["restaurants"]+'🍴', callback_data='1')
    btn2 = InlineKeyboardButton(text["places"]["hotels"]+'🏢', callback_data='2')
    btn3 = InlineKeyboardButton(text["places"]["museums"]+'🏛', callback_data='3')
    btn4 = InlineKeyboardButton(text["places"]["exhibitions"]+'🖼', callback_data='4')
    btn5 = InlineKeyboardButton(text["places"]["monuments"]+'🗿', callback_data='5')
    btn6 = InlineKeyboardButton(text["places"]["events"]+'📆', callback_data='6')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    markup.row(btn5, btn6)
    return markup
