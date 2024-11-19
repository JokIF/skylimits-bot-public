from aiogram import types
from aiogram.filters import BaseFilter

from core.utils.keyboard_texts import (button_main_menu, button_with_review, 
                                       button_how_order, button_FAQ, 
                                       button_to_conn_manager, button_items_in)

class MainMenuFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == button_main_menu
    

class ReviewsFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == button_with_review
    

class HowToOrderFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == button_how_order


class FAQFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == button_FAQ
    

class ManagerFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == button_to_conn_manager
    

class InStorageFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.text == button_items_in
