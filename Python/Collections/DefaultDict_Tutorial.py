from collections import defaultdict


n, m = map(int, raw_input().split())
groups = defaultdict(list)

for i in range(1, n+1):
    groups[raw_input()].append(str(i))
for _ in range(m):
    b = raw_input()
    if b in groups.keys():
        print ' '.join(groups[b])
    else:
        print '-1'
