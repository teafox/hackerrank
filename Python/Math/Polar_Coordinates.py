import cmath


c = eval(raw_input())
x = c.real
y = c.imag
r = cmath.sqrt(pow(x, 2) + pow(y, 2)).real
fi = cmath.phase(complex(x, y))

print r
print fi
