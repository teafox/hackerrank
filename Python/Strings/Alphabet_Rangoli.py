#def print_rangoli(size):

N = 10
n_str = ((N-1) * 2) + 1
l_str = ((N-1) * 4) + 1

for n in range(n_str):
    offset = (N - abs(((n+1) % N) - (n/N) * N)) % N
    s = chr(97 + offset)
    for c in range(1, N - offset):
        tail = chr(97 + offset + c)
        s = ''.join([tail, '-', s, '-', tail])
    tail = '-' *(offset*2)
    s = tail + s + tail
    print s

