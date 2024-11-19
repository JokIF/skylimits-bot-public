from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram import types
from aiogram import Router

from typing import Dict, Any, List, Union

from loguru import logger

from core.database import User


class SqlMiddleware(BaseMiddleware):
    async def __call__(self, 
                       handler, 
                       event: Union[types.Message, types.CallbackQuery], 
                       data: Dict[str, Any]):
        user: User = await User.query.where(User.id == event.from_user.id).gino.first()
        if user is None:
            user: User = await User.create(id=event.from_user.id,
                                           first_name=event.from_user.first_name,
                                           last_name=event.from_user.last_name,
                                           username=event.from_user.username,
                                           is_premium=event.from_user.is_premium)
        return await handler(event, data)

    def setup(self, router, *events):
        for event in events:
            router.observers[event].outer_middleware.register(self)