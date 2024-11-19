from .user_model import User, db
from .updown import on_start, on_shutdown


def setup(dp):
    dp.startup.register(on_start)
    dp.shutdown.register(on_shutdown)

__all__ = ["User", "db", "setup"]