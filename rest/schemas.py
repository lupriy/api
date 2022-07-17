from typing import Union, List

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: float
    available: Union[bool, None] = True

    class Config:
        orm_mode = True


class ItemUpdate(BaseModel):
    id: int = None
    name: str = None
    price: float = None
    available: Union[bool, None] = True

    class Config:
        orm_mode = True


class Table(BaseModel):
    id: int
    name: str
    price: int

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: int
    table_id: int
    paid: Union[bool, None] = False
    items: List[Item] = []

    class Config:
        orm_mode = True
