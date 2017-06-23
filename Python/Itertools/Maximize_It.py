from itertools import product
k, m = map(int, raw_input().split())
N = []
for _ in range(k):
    N.append(map(int, raw_input().split()[1:]))

print max(map(lambda x: sum(map(lambda x: x**2, x)), product(*N)))
