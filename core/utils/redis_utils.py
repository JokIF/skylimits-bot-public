from datetime import datetime
from logging import getLogger
from typing import Union

from core.services.cbr_api import DATE_FORMAT

logger = getLogger(name=__file__)
_key_parser = lambda key_word: ":".join(["fsm", f"{key_word}"])
RATE = "rate"
DATE = "date"


class RedisForRatesrMixin():
    async def get_date(self):
        date_str = await self.redis.get(_key_parser(DATE))
        return datetime.strptime(date_str.decode(), DATE_FORMAT) if date_str else date_str
    
    async def get_rate(self):
        rate = await self.redis.get(_key_parser(RATE))
        return rate.decode() if rate else rate
    
    async def set_rates_and_date(self, date: datetime, rate: Union[float, str]):
        await self._set_date(date)
        await self._set_rate(str(rate))
    
    async def _set_date(self, date: datetime):
        date_str = date.strftime(DATE_FORMAT)
        await self.redis.set(_key_parser(DATE), date_str)
    
    async def _set_rate(self, rate: str):
        await self.redis.set(_key_parser(RATE), rate)


# if __name__ == "__main__":
#     from core.init import redis
#     class Test(RedisToRatesrMixin):
#         def __init__(self):
#             self.redis = redis
    
#     async def main():
#         test = Test()
#         await test.set_rates_and_date(datetime.now(), 0.075173)
#         date = await test.get_date()
#         rate = await test.get_rate()
#         logger.warning(f"date: {date}\nrate: {rate}")
    
#     run(main())