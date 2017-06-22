N, X = map(int, raw_input().split())
score = []
for x in range(X):
    score.append(map(float, raw_input().split()))
for s in zip(*score):
    print sum(s)/float(X)
