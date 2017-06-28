import re

s = raw_input()
print bool(re.search('^(?!.*(.)(.)\\1\\2)'
                     '(?!.*(.).\\3(.).\\4)'
                     '[1-9]\d{5}$',
                     s))
