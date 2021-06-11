from math import pi
g = 9.81 # gravitational acceleration (m/s^2)
r = 1.2 # air density (kg/m^3)
C = 0.4 # drag coefficient
A = pi*11**2 # cross-sectional area (cm^2)
A = A*(1/100**2) # convert area to m^2
m = 0.43 # mass (kg)
V_s = 30 # velocity of soft kick (km/h)
V_s = V_s*(1000)*(1/3600) # convert to (m/s)
V_h = 120 # velocity of soft kick (km/h)
V_h = V_h*(1000)*(1/3600) # convert to (m/s)

Fg = m*g # gravitational force (N)
Fd_s = 0.5*C*r*A*V_s**2 # drag force for soft kick (N)
Fd_h = 0.5*C*r*A*V_h**2 # drag force for soft kick (N)

print('''gravitational force = %.2f N
drag force for soft kick = %.2f N
drag force for hard kick = %.2f N'''
% (Fg, Fd_s, Fd_h))

'''
Trial run:
Expected result:
gravitational force = 4.22 N
drag force for soft kick = 0.63 N
drag force for hard kick = 10.14 N
>python3 kick.py
gravitational force = 4.22 N
drag force for soft kick = 0.63 N
drag force for hard kick = 10.14 N
'''