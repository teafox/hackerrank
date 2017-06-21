def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = 'AEIOU'

    str_l = len(string)
    for p in range(len(string)):
        if string[p] in vowels:
            kevin += str_l - p
        else:
            stuart += str_l - p

    if kevin == stuart:
        print 'Draw'
        return
    if stuart > kevin:
        print 'Stuart ' + str(stuart)
    else:
        print 'Kevin ' + str(kevin)


minion_game('BANANA')
