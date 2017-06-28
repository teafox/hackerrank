import re


for _ in range(int(raw_input())):
    s = raw_input()
    print 'Valid' if all([re.search(r, s) for r in ['^[456][0-9]{3}(-?[0-9]{4}){3}$']]) \
                     and not re.search('(\d)-?\\1-?\\1-?\\1', s) else 'Invalid'
