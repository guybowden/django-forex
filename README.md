Django Forex
============

Simple foreign exchange app for Django using http://openexchangerates.org/

Populates a DB table with exchange rates from http://openexchangerates.org/

And then has two functions to use it to convert money.

install:
--------------------------------------


add `'forex'` to your applications dict
run `python manage.py syncdb`

then run the management command: 
`python manage.py updateexchangerates`

The exchange rates are updated once per hour, so you can run that management
command once per hour via Crontab or whatever you use for scheduling to keep 
rates up to date on your system.


usage:
--------------------------------------

`>>> from forex import rate, convert`
`>>> # convert 200 GBP into Euros`
`>>> convert(200, 'GBP', 'EUR')`
`239.32`
`>>> # check ex rate between GBP and EUR`
`>>> rate('GBP','EUR')`
`0.8359039482424`

simple.