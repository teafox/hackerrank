from collections import deque


N = input()
d = deque()
for _ in range(N):
    s = raw_input().split()
    command = s[0]
    args = s[1:]
    if not args:
        res = eval(''.join(['d.', command, '()']))
    else:
        eval(''.join(['d.', command, '(', ','.join(args), ')']))
print ' '.join(map(str, list(d)))
