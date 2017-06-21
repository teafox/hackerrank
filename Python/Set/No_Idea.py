n, m = map(int, raw_input().split())
arr = map(int, raw_input().split())
A = map(int, raw_input().split())
B = map(int, raw_input().split())

tmp_arr = set(arr)
A = tmp_arr & set(A)
B = tmp_arr & set(B)
happiness = 0
for ch in arr:
    if ch in A:
        happiness += 1
    elif ch in B:
        happiness -= 1
print happiness
