#!/bin/python
n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

arr.reverse()
arr = ' '.join(map(str, arr))
print arr
