from pydantic import BaseModel
from typing import Dict, List


class User(BaseModel):
    name: str
    mail: str
    address: str


class Bank(BaseModel):
    name: str
    rating: float
    opened: bool


class Card(BaseModel):
    cart_holder: User
    which_bank: Bank
    opened: bool


class Balance(BaseModel):
    card: Card
    currency_amount: List[Dict[str, int]]


user1 = User(name='Andor', mail='Andor@gmail.com',
             address='Uzbekistan, Tashkent, Yunusabad region')
bank1 = Bank(name='UzBank', rating=6.5, opened=True)
card1 = Card(cart_holder=user1, which_bank=bank1, opened=True)
balance1 = Balance(card=card1, currency_amount=[{'sum': 55000}, {'usd': 34}])