from math import sqrt, e, pi
x = 1 
m = 0 
s = 2

f_expected = 0.17603266 # calculated by hand

f = 1/(s*sqrt(2*pi))*e**(-0.5*((x-m)/s)**2)

ep = 1e-5 # epsilon of 

if abs(f-f_expected) < ep:
    print('f(x) = %.5f, accurate to epsilon = %f' % (f, ep))
else:
    print('Value not accurate to %f' % ep)

'''
Trial run:
Expected result: 0.17603266
>python3 gaussian1.py
f(x) = 0.17603, accurate to epsilon = 0.000010
'''