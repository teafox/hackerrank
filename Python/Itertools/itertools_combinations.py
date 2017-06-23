from itertools import combinations

S, k = raw_input().split()
for i in range(1, int(k)+1):
    for c in [''.join(n) for n in combinations(sorted(S), i)]:
        print c
