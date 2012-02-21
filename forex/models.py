from django.db import models

class Currency(models.Model):
    symbol = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=3,unique=True)
    rate = models.FloatField(default=1.0)
    base = models.CharField(max_length=3)
    
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.code)
    
    def convert_to(self, currency, amount=1):
        return  amount * (currency.rate / self.rate)
        


def update_currency(code, name, rate, base):
    currency, created = Currency.objects.get_or_create(code=code)
    currency.base = base
    currency.name = name
    currency.rate = rate
    currency.save()