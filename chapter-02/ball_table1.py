from sympy import (symbols, lambdify)
from pprint import  pprint
a = 0
b = 2
n = 4
h = (b - a)/n

T, t, v0, g = symbols('T t v0 g')

T = [(a+i*h)*v0/g for i in range(n+1)]
Y = [v0*t - (1/2)*g*t**2 for t in T]
table = [[t, y] for t, y in zip(T, Y)]

for i in table:
    i[0] = 't = ' + str(i[0])
    i[1] = 'y = ' + str(i[1])

pprint(table)