n = int(raw_input().strip())
n_strings = [raw_input().strip() for _ in range(n)]
q = int(raw_input().strip())
q_queries = [raw_input().strip() for _ in range(q)]

for que in q_queries:
    print n_strings.count(que)
