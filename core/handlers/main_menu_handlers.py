from aiogram import types
from aiogram.filters.command import CommandStart, Command
from aiogram.filters import or_f
from aiogram.fsm.context import FSMContext
from magic_filter import F

from core.init import dp, sql_router
from core.utils.keyboards import KeyboardData, main_menu_keyboard, review_keyboard, how_to_order_keyboard, FAQ_keyboard, manager_keyboard, in_storage_keyboard
from core.utils.states import MainMenuStates, CalculateStates
from core.filters.main_menu_filters import MainMenuFilter, ReviewsFilter, HowToOrderFilter, FAQFilter, ManagerFilter, InStorageFilter


async def main_menu_handler(message: types.Message, state: FSMContext):
    user = message.chat.full_name
    await message.answer(**main_menu_keyboard(user))
    await state.clear()
    await state.set_state(MainMenuStates.main)

@dp.message(MainMenuFilter())
@dp.message(CalculateStates.enter_price, or_f(Command("start"), Command("menu")))
@sql_router.message(Command("menu"))
@sql_router.message(CommandStart())
async def main_menu_message_handler(message: types.Message, state: FSMContext):
    await main_menu_handler(message, state)

@dp.callback_query(KeyboardData.filter(F.action == "menu"))
async def main_menu_callback_handler(callbackq: types.CallbackQuery, state: FSMContext):
    await main_menu_handler(callbackq.message, state)

@dp.message(MainMenuStates.main, ReviewsFilter())
async def review_handler(message: types.Message, state: FSMContext):
    await message.answer(**review_keyboard())
    await state.set_state(MainMenuStates.review)

@dp.message(MainMenuStates.main, HowToOrderFilter())
async def how_to_handler(message: types.Message, state: FSMContext):
    await message.answer(**how_to_order_keyboard())
    await state.set_state(MainMenuStates.HowToOrder)

@dp.message(MainMenuStates.main, FAQFilter())
async def FAQ_handler(message: types.Message, state: FSMContext):
    await message.answer(**FAQ_keyboard())
    await state.set_state(MainMenuStates.FAQ)

@dp.message(MainMenuStates.main, ManagerFilter())
async def manager_handler(message: types.Message, state: FSMContext):
    await message.answer(**manager_keyboard())
    await state.set_state(MainMenuStates.manager)

@dp.message(MainMenuStates.main, InStorageFilter())
async def in_storage_handler(message: types.Message, state: FSMContext):
    await message.answer(**in_storage_keyboard())
    await state.set_state(MainMenuStates.in_storage)