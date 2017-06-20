arg = map(int, raw_input().strip().split(' '))
N, Q = tuple(arg)
lastAnswer = 0
seqList = [[] for _ in range(N)]
Queries = [[] for _ in range(Q)]

for q in range(Q):
    Queries[q] = map(int, raw_input().strip().split(' '))

for que in Queries:
    sq_type, x, y = tuple(que)
    index = ((x ^ lastAnswer) % N)
    if sq_type == 1:
        seqList[index].append(y)
    if sq_type == 2:
        lastAnswer = seqList[index][y % len(seqList[index])]
        print lastAnswer
