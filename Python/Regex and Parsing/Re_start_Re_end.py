import re

s = raw_input()
k = raw_input()

p = re.compile(k)
m = p.search(s)
if m:
    while m:
        print (m.start(), m.end() - 1)
        m = p.search(s, m.start()+1)
else:
    print (-1, -1)
