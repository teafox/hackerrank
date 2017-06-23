from itertools import permutations

S, k = raw_input().split()
arr = sorted([''.join(n) for n in permutations(S, int(k))])
for c in arr:
    print c
