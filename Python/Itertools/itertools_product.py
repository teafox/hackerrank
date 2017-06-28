import itertools
a = map(int, raw_input().split())
b = map(int, raw_input().split())

print ' '.join(str(n) for n in itertools.product(a, b))
