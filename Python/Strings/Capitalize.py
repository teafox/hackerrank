def capitalize(string):
    return ' '.join(map(str.capitalize, string.split(' ')))

s = 'hello   world  lol'
print capitalize(s)
