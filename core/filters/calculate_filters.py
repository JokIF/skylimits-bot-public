from typing import Any
from aiogram.filters import BaseFilter
from aiogram import types
from core.utils.keyboard_texts import button_to_calculate, button_shoes_and_top, button_sweatshirt_and_pants, button_shirt_and_shorts


class To_calculate(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == button_to_calculate
    
class Choose_calculate(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == button_shoes_and_top \
        or message.text == button_shirt_and_shorts \
        or message.text == button_sweatshirt_and_pants