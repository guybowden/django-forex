"""
A management command which updates exchange rates from http://openexchangerates.org/latest.json

"""
import json, urllib

from django.core.management.base import NoArgsCommand

from forex.models import update_currency


class Command(NoArgsCommand):
    help = "Updates exchange rates from http://openexchangerates.org/latest.json"

    def handle_noargs(self, **options):
        print "Downloading rates http://openexchangerates.org/latest.json"
        url = "http://openexchangerates.org/latest.json"
        print "Parsing rates..."
        rates_result = json.load(urllib.urlopen(url))
        
        print "Downloading currency names http://openexchangerates.org/currencies.json"
        url = "http://openexchangerates.org/currencies.json"
        print "Parsing names..."
        currencies = json.load(urllib.urlopen(url))
        
        print "updating currencies"
        
        base = rates_result['base']
        rates = rates_result['rates']
        
        for code, rate in rates.iteritems():
            name = currencies[code]
            print "Updating %s (%s) to: %s" % (name, code, rate)
            update_currency(code, name, rate, base)
        
        print "Finished"