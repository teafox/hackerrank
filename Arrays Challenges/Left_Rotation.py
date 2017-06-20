arg = map(int, raw_input().strip().split(' '))
array = map(int, raw_input().strip().split(' '))
n, d = tuple(arg)
print ' '.join(map(str, array[d:] + array[:d]))
