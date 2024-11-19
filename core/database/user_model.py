from gino import Gino
from sqlalchemy import String, Column, ForeignKey, Boolean, BigInteger

db = Gino()


class User(db.Model):
    __tablename__ = 'user'
    id = Column(BigInteger(), nullable=False, autoincrement=False, primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=True)
    username = Column(String(), nullable=True)
    language = Column(String(), nullable=True)
    is_premium = Column(Boolean(), nullable=True)


class RelateUser(db.Model):
    __abstract__ = True
    user_id = Column(BigInteger(), ForeignKey(User.id), unique=True, nullable=False)