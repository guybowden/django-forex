from django.conf import settings

# get an api key from openexchangerates.org
OPENEXCHANGERATES_API_KEY = getattr(settings, 'OPENEXCHANGERATES_API_KEY', 'apikey')

# limit the currencies that the API exposes
ALLOWED_CURRENCIES = getattr(settings, 'ALLOWED_CURRENCIES', None)
