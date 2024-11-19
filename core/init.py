from aiogram import Router, Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis 

from core import config

from logging import getLogger

logger = getLogger(name=__file__)

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    password=config.REDIS_PASSWORD
)
storage = RedisStorage(redis=redis)
bot = Bot(config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=storage)

sql_router = Router(name="sql")
calculate_router = Router(name="calculate")


async def notify_all_working(bot: Bot):
    logger.info('all working')


def setup():
    import core.handlers
    dp.include_router(calculate_router)
    dp.include_router(sql_router)

    import core.middlewares as middlewares
    middlewares.setup(dp)

    import core.database as database
    database.setup(dp)
    
    dp.startup.register(notify_all_working)
