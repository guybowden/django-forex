from models import Currency
from serializers import CurrencySerializer
from rest_framework import generics

import settings


class CurrencyList(generics.ListAPIView):
    model = Currency
    serializer_class = CurrencySerializer

    def get_queryset(self):
        queryset = super(CurrencyList, self).get_queryset()
        if settings.ALLOWED_CURRENCIES:
            queryset = queryset.filter(code__in=settings.ALLOWED_CURRENCIES)

        return queryset


class CurrencyDetail(generics.RetrieveAPIView):
    model = Currency
    serializer_class = CurrencySerializer
