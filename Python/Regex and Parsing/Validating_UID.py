import re


for _ in range(int(raw_input())):
    s = raw_input()
    print 'Valid' if all([re.search(r, s) for r in ['[a-zA-Z0-9]{10}', '([A-Z].*){2}', '([0-9].*){3}', ]]) \
                     and not re.search('.*(.).*\\1.*', s) else 'Invalid'
