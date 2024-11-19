from aiohttp import ClientSession

from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal

from logging import getLogger


logger = getLogger(name=__file__)
DATE_FORMAT = "%Y-%m-%d"


class CbrApi:
    URL = "https://www.cbr-xml-daily.ru/latest.js"

    @property
    def _get_url(self):
        return self.URL

    async def __get_data(self):
        async with ClientSession() as session:
            async with session.get(self._get_url) as response:
                if response.status == 200:
                    logger.info(f"requist {self.URL}")
                    return await response.json(content_type="application/javascript")
                err = response.json
                logger.exception(err)

    async def get_CNY_rate(self):
        response = await self.__get_data()
        rate = "{:.3f}".format(Decimal(1) / Decimal(response["rates"]["CNY"]))
        return rate
    
        

    