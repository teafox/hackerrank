def print_formatted(number):
    f_len = len(bin(number)[2:])
    for i in range(1, number+1):
        print ('{:>%d} {:>%d} {:>%d} {:>%d}' %
               (f_len, f_len, f_len, f_len)).format(i, oct(i).lstrip('0'), hex(i).upper()[2:], bin(i)[2:])

print_formatted(17)
