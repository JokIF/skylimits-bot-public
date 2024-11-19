from .user_model import db

from aiogram import Dispatcher, Bot
from gino.exceptions import UninitializedError
from logging import getLogger

from core import config


logger = getLogger(name=__file__)

async def on_start(bot: Bot):
    logger.info(f'db connecting')
    try:
        await db.set_bind(config.POSTGRESQL_URL)
    except UninitializedError:
        logger.exception('Gino engine is not initialized')


async def on_shutdown(bot: Bot):
    bind = db.pop_bind()
    if bind:
        logger.info('db unbinding')
        try:
            await bind.close()
        except UninitializedError:
            logger.exception('Gino engine is not initialized')