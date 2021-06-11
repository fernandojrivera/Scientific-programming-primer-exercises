M = 67 # mass (g)
r = 1.038 # density (g/cm^3)
c = 3.7 # specific heat capacity (J/gK)
K = 5.4e-3 # thermal conductivity (W/cmK)
Tw = 100 # temperature of water
To = [4, 20] # original temperature of the egg
Ty = 70 # final temperature of the egg

from math import log, pi

t_0 = ((M**(2/3) * c * r**(1/3))/(K*pi**(2)*(4*pi/3)**(2/3))) * log(0.76*(To[0] - Tw)/(Ty - Tw))
t_1 = ((M**(2/3) * c * r**(1/3))/(K*pi**(2)*(4*pi/3)**(2/3))) * log(0.76*(To[1] - Tw)/(Ty - Tw))
t_0, t_1 = t_0 / 60, t_1/60 # convert to minutes

print('''fridge temperature egg = %.2f min
room temperature egg = %.2f min
''' %(t_0, t_1))

'''
Trial run:
Expected result:
fridge temperature egg = 6.61 min
room temperature egg = 5.25 min
>python3 egg.py
fridge temperature egg = 6.61 min
room temperature egg = 5.25 min
'''