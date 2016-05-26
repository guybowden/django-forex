"""
A management command which updates exchange rates from http://openexchangerates.org/api/latest.json

"""
import json, urllib

from django.core.management.base import NoArgsCommand

from forex.models import update_currency
from forex.settings import OPENEXCHANGERATES_API_KEY


class Command(NoArgsCommand):
    help = "Updates exchange rates from http://openexchangerates.org/latest.json"

    def handle_noargs(self, **options):
        print "Downloading rates http://openexchangerates.org/api/latest.json"
        url = "http://openexchangerates.org/api/latest.json?app_id=%s" % OPENEXCHANGERATES_API_KEY
        print "Parsing rates..."
        rates_result = json.load(urllib.urlopen(url))

        print "Downloading currency names http://openexchangerates.org/api/currencies.json"
        url = "http://openexchangerates.org/api/currencies.json?app_id=%s" % OPENEXCHANGERATES_API_KEY
        print "Parsing names..."
        currencies = json.load(urllib.urlopen(url))

        print "updating currencies"

        base = rates_result['base']
        rates = rates_result['rates']

        for code, rate in rates.iteritems():

            try:
                name = currencies[code]
            except KeyError:
                name = code

            update_currency(code, name, rate, base)

        print "Finished"
