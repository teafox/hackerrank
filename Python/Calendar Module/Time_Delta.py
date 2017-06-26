import time

t = int(raw_input())
for _ in range(t):
    s1 = raw_input()
    t1 = time.strptime(s1, '%a %d %b %Y %H:%M:%S %z')
    s2 = raw_input()
    t2 = time.strptime(s2, '%a %d %b %Y %H:%M:%S %z')
    print time.mktime(t1) - time.mktime(t2)

