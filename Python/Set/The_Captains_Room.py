k = int(raw_input())
arr = map(int, raw_input().split())

new_set = set(arr)
print (sum(new_set)*k - sum(arr))/(k-1)
