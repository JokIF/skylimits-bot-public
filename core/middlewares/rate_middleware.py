from aiogram import types
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from typing import Any, Awaitable, Callable, Coroutine, Dict, Union
from datetime import datetime
from logging import getLogger

from core.init import redis
from core.utils.redis_utils import RedisForRatesrMixin
from core.services.cbr_api import CbrApi
from core.config import markup_on_rate


logger = getLogger(name=__file__)

class CheckRateMiddleware(RedisForRatesrMixin, BaseMiddleware):
    def __init__(self):
        self.redis = redis
        self.delay = False
        self.cbr_api = CbrApi()

    async def __call__(
                self, 
                handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
                event: Union[types.Message, types.CallbackQuery], 
                data: Dict[str, Any]
                ):
        date = await self.get_date()
        if not date or datetime.now().date() - date.date():
            cbr_rate = await self.cbr_api.get_CNY_rate()
            await self.set_rates_and_date(datetime.now(), cbr_rate)
        else:
            cbr_rate = await self.get_rate()
        data["rate_CNY"] = float(cbr_rate) + markup_on_rate
        return await handler(event, data)
        
    def setup(self, router, *events):
        for event in events:
            router.observers[event].outer_middleware.register(self)
