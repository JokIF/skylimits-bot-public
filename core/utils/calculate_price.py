from core.utils import keyboard_texts
from core.config import (markup_on_order, 
                         markup_shoes_and_top, 
                         markup_shirt_and_shorts, 
                         markup_sweatshirt_and_pants)

import re
from logging import getLogger


logger = getLogger(__file__)

catigory_to_price = {
    keyboard_texts.button_shirt_and_shorts: markup_shirt_and_shorts,
    keyboard_texts.button_shoes_and_top: markup_shoes_and_top,
    keyboard_texts.button_sweatshirt_and_pants: markup_sweatshirt_and_pants
}

def check_price_num(num: str):
    return bool(re.fullmatch(r"\d+", num))


def calculate_price(base_price: int, rate: float, catigory: str):    
    price = 0 #your formula
    return price
