from core.config import manager_tag, review_group_tag, FAQ_link, how_to_link, manager_link, in_stock_group_tag

# Main menu
button_to_calculate = "💵Рассчитать стоимость"
button_with_review = "🎯Отзывы"
button_to_conn_manager = "📲Связь с менеджером"
button_how_order = "🚚Как заказать?"
button_FAQ = "❓F.A.Q"
button_sales = "‼️Акции‼️"
button_items_in = "🎒Товары в наличии"

# Calculate
button_shoes_and_top = "👟Обувь/Верхняя одежда"
button_sweatshirt_and_pants = "👖Толстовки/Штаны"
button_shirt_and_shorts = "👕Футболка/Шорты"
button_manager = "✅Оформить заказ"

# Universal
button_main_menu = "♻️Меню"

def text_main_menu(user):
    return f"""Привет, {user}

Тут ты можешь рассчитать сумму своего заказа💵 
<a href='{manager_link}'>Связаться с менеджером</a> 
Получить ответы на все свои вопросы🤔"""


def text_choose_catigory():
    return "Выбери категорию товара"

def text_pre_calculate(exchange_rate, selected_category):
    return """Введи цену на {} в <b>юанях</b>, а я рассчитаю конечную стоимость
Курс ¥ - {:.2f}₽""".format(selected_category, exchange_rate)

def text_post_calculate(price, rate, base_price):
    return f"""Итоговая стоимость позиции: {price}₽


Стоимость включает: 

Стоимость товара - {(base_price * rate):.2f}₽
Доставка 🚚 Китай-Уссурийск - 675₽/кг
Комиссия нашего сервиса - 1000₽
Курс ¥ - {rate:.2f}

Стоимость рассчитана до нашего склада в <b>Уссурийске</b>
Доставка до вашего города оплачивается <b>при получении</b> в пункте выдачи заказов.
Если вы покупаете более 2-х товаров, то стоимость каждого следующего товара будет со скидкой

👟 Обувь/Верхняя одежда: -300₽
👖Толстовка/штаны: -200₽
👕/🩳Футболка/шорты: -100₽
"""


def text_review():
    return f"""Отзывы: {review_group_tag}"""

def text_FAQ():
    return f"""Ответы на часто задаваемые вопросы: {FAQ_link}"""

def text_how_to():
    return f"""
Перед оформлением заказа прочтите данную статью: 
{how_to_link}
"""

def text_manger():
    return f"""Менеджер: {manager_tag}"""


def text_in_storage():
    
    return f"""Товары в наличии: {in_stock_group_tag}"""


def text_enter_num():
    return "Введите Число"
