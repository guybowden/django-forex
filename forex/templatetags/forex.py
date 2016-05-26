from django import template
from ..forex import convert as convert_

register = template.Library()


@register.simple_tag
def convert(amount, from_currency, to_currency, show_decimals=False):
    amt = convert_(amount, from_currency, to_currency)
    if show_decimals:
        return amt
    else:
        return int(amt)
