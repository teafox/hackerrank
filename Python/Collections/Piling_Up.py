from collections import deque

t = int(raw_input())
for _ in range(t):
    n = int(raw_input())
    d = deque(map(int, raw_input().split()))
    last = None
    for i in range(n):
        if not last or d[0] <= last and d[-1] <= last:
            if d[0] >= d[-1]:
                last = d[0]
                d.popleft()
            elif d[-1] > d[0]:
                last = d[-1]
                d.pop()
        else:
            print 'No'
            break
    if len(d) == 0:
        print 'Yes'

