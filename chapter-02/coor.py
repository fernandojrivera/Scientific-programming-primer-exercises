a = 0
b = 10
n = 4
h = (b - a)/n
x = []
for i in range(n+1):
    x.append(a+i*h)
    print(x[i], end=' ')

#alternate solution
x_comprehension = [a+i*h for i in range(n+1)]