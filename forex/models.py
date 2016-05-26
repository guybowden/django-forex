import copy
import datetime
from django.db import models


class CurrencyManager(models.Manager):
    _cache = None

    def cached_values(self):
        if not self._cache:
            fields = ('id', 'symbol', 'name', 'code')
            self._cache = tuple(self.values(*fields))
        # copy, because we cannot freeze dictionary
        return copy.deepcopy(self._cache)


class Currency(models.Model):
    symbol = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=3, unique=True)
    rate = models.FloatField(default=1.0)
    base = models.CharField(max_length=3)

    objects = CurrencyManager()

    def __unicode__(self):
        return u'%s' % self.code

    def convert_to(self, currency, amount=1):
        return amount * (currency.rate / self.rate)

    def get_rate_for_date(self, date):
        # should try and get the next date along
        qs = self.currencyhistory_set.filter(date__gte=date).order_by('date')
        if qs.exists():
            return qs[0].rate

        # or perhaps the other way..
        qs = self.currencyhistory_set.filter(date__lte=date).order_by('-date')
        if qs.exists():
            return qs[0].rate

        # nope! just give them the rate as it is now..
        return self.rate


class CurrencyHistory(models.Model):
    """ stores the currency as it was at the *date* """
    currency = models.ForeignKey(Currency)
    date = models.DateField()
    rate = models.FloatField(default=1.0)


def update_currency(code, name, rate, base):
    currency, created = Currency.objects.get_or_create(code=code)
    currency.base = base
    currency.name = name
    currency.rate = rate
    currency.save()

    # now store the historical record by date - that way the last fetch of the day will always be the one we keep.
    currency_history, created = CurrencyHistory.objects.get_or_create(
        currency=currency, date=datetime.date.today()
    )
    currency_history.rate = rate
    currency_history.save()
