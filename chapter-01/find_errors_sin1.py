#sin is not a standard function, must be imported from the math module
from math import sin
x=1; print('sin(%g)=%g' % (x, sin(x)))

'''
Trial run:
Expected result: sin(1)=0.841471
>python3 find_errors_sin1.py
sin(1)=0.841471
'''