from printer import Printer
from database import create_db, Session
import requests
from bs4 import BeautifulSoup


def create_database():
    create_db()
    _load_printer_data(Session())


def _load_printer_data(session: Session):
    url = 'https://price.ru/mfu-printery-kopiry/xerox/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    item_list = soup.find_all("div", class_="p-card p-card__model p-card__tile")
    for item in item_list:
        item_name = item.find('div', class_='p-card__title text-body-m-book').text.strip()
        item_price = _get_digit_from_str(
            item.find('span', class_='p-card__price--new text-subtitle-price-bold').text.strip()
        )
        print = Printer(item_name, item_price)
        session.add(print)
    session.commit()
    session.close()


def _get_digit_from_str(input_str: str):
    res = ''
    for item in input_str:
        if item.isdigit():
            res += item

    return int(res)
