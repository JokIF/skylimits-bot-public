from aiogram import Dispatcher

from logging import getLogger

from core.middlewares.rate_middleware import CheckRateMiddleware
from core.middlewares.sql_middleware import SqlMiddleware


logger = getLogger(name=__file__)

def setup(dp: Dispatcher):
    defaulte_events = ["message", "callback_query"]
    sql_router = dp.sub_routers[1]
    calculate_router = dp.sub_routers[0]
    
    SqlMiddleware().setup(sql_router, *defaulte_events)
    CheckRateMiddleware().setup(calculate_router, *defaulte_events)
