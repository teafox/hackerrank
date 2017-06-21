n = raw_input()
N = set(map(int, raw_input().split()))
m = raw_input()
M = set(map(int, raw_input().split()))

print len(N ^ M)
