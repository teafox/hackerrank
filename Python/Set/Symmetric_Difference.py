n = map(int, raw_input().strip())
N = map(int, raw_input().split())
m = map(int, raw_input().strip())
M = map(int, raw_input().split())

N = set(N)
M = set(M)

D = N.difference(M)
D = D.union(M.difference(N))
D = list(D)
D.sort()
for d in D:
    print d
