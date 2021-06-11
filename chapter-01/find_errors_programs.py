#1.9
#find_errors_programs.py

'''
a)
from math import sin, cos <- correct import of sin and cos functions
x = pi/4 <- correct variable assignment
1_val = math.sin^2(x) + math.cos^2(x) <-invalid variable name (starting with number), invalid power operator (should be **), invalid order of power operator (should be after the function parameters)
print(1_VAL) <- variable declaration and call should be in same case.
'''
from math import sin, cos
x = pi/4
f = sin(x)**2 + cos(x)**2
print(f)

'''
b)
v0 = 3 m/s <- units should not be included in variable declarations
t = 1 s
a = 2 m/s**2
s = v0.t + 0,5.a.t**2 <- invalid product operator (should be *). invalid decimal point (should be dot)
print(s)
'''
v0 = 3
t = 1
a = 2
s = v0*t + 0.5*a*t**2
print(s)


'''
c)
a = 3,3 b = 5,3 <- invalid decimal point (should be dot)
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2ab + b2 <- product should be explicitly declared *
eq2_sum = a2 - 2ab + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print('First equation: %g = %g', % (eq1_sum, eq1_pow)) <- no comma needed
print('Second equation: %h = %h', % (eq2_pow, eq2_pow)) <- h is not a valid number format
'''
a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print('First equation: %g = %g' %(eq1_sum, eq1_pow))
print('Second equation: %g = %g' %(eq2_pow, eq2_pow))