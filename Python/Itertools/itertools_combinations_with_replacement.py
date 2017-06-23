from itertools import combinations_with_replacement

S, k = raw_input().split()
for c in [''.join(n) for n in combinations_with_replacement(sorted(S), int(k))]:
    print c
