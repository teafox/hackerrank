#!/bin/python


arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

n = len(arr)
m = len(arr[0])

max_hourglass = None
for i in range(n-2):
    for j in range(m-2):
        hourglass = (arr[i][j] + arr[i][j+1] + arr[i][j+2]
                     + arr[i+1][j+1]
                     + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        if max_hourglass is None:
            max_hourglass = hourglass
        elif hourglass > max_hourglass:
            max_hourglass = hourglass
print str(max_hourglass)
