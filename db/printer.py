from sqlalchemy import Column, Integer, String
from database import Base


class Printer(Base):
    __tablename__ = 'printer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'название {self.name}: цена от {self.price}'
