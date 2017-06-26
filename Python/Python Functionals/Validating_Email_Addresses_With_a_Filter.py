import re


def fun(s):
    return re.match('^[\w\-]+@[a-z0-9]+\.[a-z]{1,3}$', s)


emails = ['its@gmail.com1',
          'mike13445@yahoomail9.server',
          'rase23@ha_ch.com',
          'daniyal@gmail.coma',
          'thatisit@thatisit',
          ]
print filter(fun, emails)
