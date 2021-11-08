from sympy import symbols,integrate

y, t, g, v, vo = symbols('y t g v vo') # variables for free fall

v = vo - integrate(g,t) # set equation for first derivative with constant v(0)=vo
y = integrate(v, t) # integrate velocity to get distance travelled
print('y =',y)
'''
Trial run:
Expected result: y = vo*t - (gt^2)/2
>python3 trajectory.py
y = -g*t**2/2 + t*vo
'''