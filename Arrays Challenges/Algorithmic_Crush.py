N, M = [int(n) for n in raw_input().split(" ")]
array = [0]*N
for _ in range(M):
    a, b, k = [int(n) for n in raw_input().split(" ")]
    for n in range(a-1, b):
        array[n] = array[n] + k
print max(array)
