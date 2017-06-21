A = set(map(int, raw_input().split()))
n = int(raw_input())
res = True
for _ in range(n):
    S = set(map(int, raw_input().split()))
    if not S <= A or S == A:
        res = False
print res
