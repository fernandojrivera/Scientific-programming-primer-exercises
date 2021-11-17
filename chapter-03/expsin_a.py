def g(t):
    ''' calculate a simple mathematical 1-variable function with one parameter '''
    from math import sin, pi, exp
    a = 10
    f = exp(-a*t)*sin(pi*t)
    return f

print('g(0)={a:#0.2}, g(1)={b:#0.2}'.format(a=g(0), b=g(1)))

