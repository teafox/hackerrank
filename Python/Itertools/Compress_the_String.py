from itertools import groupby

S = raw_input()
gr = [(len(list(g)), int(k)) for k, g in groupby(S)]
print ' '.join(map(str, gr))
