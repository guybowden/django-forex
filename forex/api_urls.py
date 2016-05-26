from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import api_views

urlpatterns = patterns(
    '',
    url(r'^currencies/$',
        api_views.CurrencyList.as_view(), name='currency-list'),
    url(r'^currencies/(?P<pk>[0-9]+)/$',
        api_views.CurrencyDetail.as_view(), name='currency-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
