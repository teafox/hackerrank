import re


n, m = map(int, raw_input().split())
msg = ['']*m
for _ in range(n):
    s = raw_input()
    for i in range(m):
        msg[i] += s[i]

print re.sub('(?<=\w)[^\w]+(?=\w)', ' ', ''.join(msg))
