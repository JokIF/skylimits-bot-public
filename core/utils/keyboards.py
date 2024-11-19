from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton, KeyboardButton

from core.utils import keyboard_texts
from core.config import manager_id


parse_to_kwargs = lambda text, reply_markup: {"text":text, "reply_markup": reply_markup}


class KeyboardData(CallbackData, prefix="my"):
    action: str


def main_menu_keyboard(user):
    builder = ReplyKeyboardBuilder([
        [
            KeyboardButton(text=keyboard_texts.button_to_calculate)
        ],
        [
            KeyboardButton(text=keyboard_texts.button_with_review),
            KeyboardButton(text=keyboard_texts.button_to_conn_manager)
        ],
        [
            KeyboardButton(text=keyboard_texts.button_how_order),
            KeyboardButton(text=keyboard_texts.button_FAQ)
        ],
        [
            KeyboardButton(text=keyboard_texts.button_items_in)
        ]
    ])
    text = keyboard_texts.text_main_menu(user)

    return parse_to_kwargs(text, ReplyKeyboardMarkup(resize_keyboard=True, keyboard=builder.export()))


def choose_catigory_keyboard():
    builder = ReplyKeyboardBuilder([
        [
            KeyboardButton(text=keyboard_texts.button_shoes_and_top),
            KeyboardButton(text=keyboard_texts.button_sweatshirt_and_pants)
        ],
        [
            KeyboardButton(text=keyboard_texts.button_shirt_and_shorts)
        ]
    ])
    text = keyboard_texts.text_choose_catigory()

    return parse_to_kwargs(text, ReplyKeyboardMarkup(resize_keyboard=True, keyboard=builder.export()))


def pre_convert_keyboard(exchange_rate, selected_category):
    builder = ReplyKeyboardBuilder([
        [
            KeyboardButton(text=keyboard_texts.button_main_menu)
        ]
        ])
    text = keyboard_texts.text_pre_calculate(exchange_rate, selected_category)

    return parse_to_kwargs(text, ReplyKeyboardMarkup(resize_keyboard=True, keyboard=builder.export()))


def calculated_price_keyboard(price, rate, base_price):
    builder = InlineKeyboardBuilder([
        [
            InlineKeyboardButton(text=keyboard_texts.button_manager,
                                 url=f"tg://user?id={manager_id}")
        ],
        [
            InlineKeyboardButton(text=keyboard_texts.button_to_calculate,
                                 callback_data=KeyboardData(action="calculate").pack()),
            InlineKeyboardButton(text=keyboard_texts.button_main_menu, 
                                 callback_data=KeyboardData(action="menu").pack())
        ]
    ])
    text = keyboard_texts.text_post_calculate(price, rate, base_price)

    return parse_to_kwargs(text, InlineKeyboardMarkup(inline_keyboard=builder.export()))


def review_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton(text=keyboard_texts.button_main_menu)
        ]
    ])
    text = keyboard_texts.text_review()

    return parse_to_kwargs(text, keyboard)

def how_to_order_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton(text=keyboard_texts.button_main_menu)
        ]
    ])
    text = keyboard_texts.text_how_to()

    return parse_to_kwargs(text, keyboard)

def FAQ_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton(text=keyboard_texts.button_main_menu)
        ]
    ])
    text = keyboard_texts.text_FAQ()

    return parse_to_kwargs(text, keyboard)

def manager_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton(text=keyboard_texts.button_main_menu)
        ]
    ])
    text = keyboard_texts.text_manger()

    return parse_to_kwargs(text, keyboard)

def in_storage_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton(text=keyboard_texts.button_main_menu)
        ]
    ])
    text = keyboard_texts.text_in_storage()

    return parse_to_kwargs(text, keyboard)
