from django.contrib import admin
from models import Currency


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'code', 'rate')


admin.site.register(Currency, CurrencyAdmin)
