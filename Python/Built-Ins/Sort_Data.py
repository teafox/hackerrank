N, M = map(int, raw_input().split())
table = []
for _ in range(N):
    table.append(map(int, raw_input().split()))
k = int(raw_input())

for row in sorted(table, key=lambda x: x[k]):
    print ' '.join(map(str, row))
