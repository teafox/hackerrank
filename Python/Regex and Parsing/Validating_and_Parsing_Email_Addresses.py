import re

p = re.compile('^<[\w\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>$')
for _ in range(int(raw_input())):
    s = raw_input()
    name, email = s.split()
    if p.search(email) is not None:
        print s
