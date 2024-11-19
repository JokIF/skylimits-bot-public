from aiogram.fsm.state import State, StatesGroup


class MainMenuStates(StatesGroup):
    main = State()
    review = State()
    manager = State()
    FAQ = State()
    HowToOrder = State()
    in_storage = State()

class CalculateStates(StatesGroup):
    choose_catigory = State()
    enter_price = State()