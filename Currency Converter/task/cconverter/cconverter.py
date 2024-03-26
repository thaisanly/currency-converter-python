import requests

exchange_rates = {}


def is_has_catch(currency_code):
    global exchange_rates

    return exchange_rates.get(currency_code.lower())


def get_exchange_rate(currency_code):
    global exchange_rates

    if not exchange_rates.get(currency_code.lower()):
        response = requests.get(f"http://www.floatrates.com/daily/{currency_code.lower()}.json")
        data = response.json()
        exchange_rates[currency_code.lower()] = data
    else:
        data = exchange_rates.get(currency_code.lower())

    return data


get_exchange_rate('usd')
get_exchange_rate('eur')

from_currency = input()

while True:
    to_currency = input()

    if not to_currency:
        break

    amount = float(input())

    exchange_rate = is_has_catch(to_currency)

    print("Checking the cache...")
    if exchange_rate:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        exchange_rate = get_exchange_rate(to_currency)

    rate = exchange_rate[from_currency.lower()]['inverseRate']

    to_amount = round(rate * amount, 2)

    print("You received {total} {currency}".format(total=to_amount, currency=to_currency.upper()))
