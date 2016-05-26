from models import Currency


def convert(amount, from_currency, to_currency, raw_val=False):
    """ converts an amount from one currency to another -
        pass "raw_val=True" if you want the non 2 decimal rounded version
    """

    if isinstance(from_currency, str):
        from_currency = Currency.objects.get(code=from_currency)

    if isinstance(to_currency, str):
        to_currency = Currency.objects.get(code=to_currency)

    converted = from_currency.convert_to(to_currency, amount)

    if raw_val:
        return converted

    return round(converted * 100) / 100


def rate(from_, to):
    return convert(1, to, from_, True)
