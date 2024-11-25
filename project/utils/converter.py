from currency_converter import CurrencyConverter
from datetime import date

c = CurrencyConverter()

def convert(amount, from_currency, to_currency):
    date_of_converter = date(year=2022, month=2, day=24)  # date_of_converter = date.today()
    r = c.convert(amount, from_currency, to_currency, date=date_of_converter)
    return r
