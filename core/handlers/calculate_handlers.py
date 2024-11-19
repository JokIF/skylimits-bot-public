from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.filters import or_f
from magic_filter import F

from core.filters.calculate_filters import To_calculate, Choose_calculate
from core.init import calculate_router, dp
from core.utils.keyboards import KeyboardData, pre_convert_keyboard, choose_catigory_keyboard, calculated_price_keyboard
from core.utils.states import MainMenuStates, CalculateStates
from core.utils.calculate_price import calculate_price, check_price_num
from core.utils.keyboard_texts import text_enter_num
from core.config import ASSETS_DIR


async def pre_calculate_menu_handler(message: types.Message, state: FSMContext):
    photo1 = types.BufferedInputFile.from_file(ASSETS_DIR / "photo1.jpg", "photo1")
    photo2 = types.BufferedInputFile.from_file(ASSETS_DIR / "photo2.jpg", "photo2")
    await message.answer_media_group(media=[
        types.InputMediaPhoto(media=photo1), 
        types.InputMediaPhoto(media=photo2)
        ])
    await message.answer(**choose_catigory_keyboard())
    await state.set_state(CalculateStates.choose_catigory)

@dp.message(To_calculate(), MainMenuStates.main)
async def pre_calculate_menu_message_handler(message: types.Message, state: FSMContext):
    await pre_calculate_menu_handler(message, state)

@dp.callback_query(KeyboardData.filter(F.action == "calculate"))
async def pre_calculate_menu_callback_handler(callbackq: types.CallbackQuery, state: FSMContext):
    await pre_calculate_menu_handler(callbackq.message, state)


@calculate_router.message(Choose_calculate(), CalculateStates.choose_catigory)
async def enter_price_handler(message: types.Message, rate_CNY, state: FSMContext):
    await state.set_data({"catigory": message.text})
    await message.answer(**pre_convert_keyboard(rate_CNY, message.text))
    await state.set_state(CalculateStates.enter_price)

@calculate_router.message(CalculateStates.enter_price)
async def calculate_price_handler(message: types.Message, rate_CNY, state: FSMContext):
    if not check_price_num(message.text):
        await message.answer(text=text_enter_num())
        await message.delete()
        return
    state_data = await state.get_data()
    price = calculate_price(
        int(message.text),
        rate_CNY,
        state_data.get("catigory")
        )
    
    await message.answer(**calculated_price_keyboard(int(price), float(rate_CNY), int(message.text)))
    await state.clear()