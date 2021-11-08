m_e = 9.1094*10**-31 #  Kg
e = 1.6022*10**-19 #  C
ep_0 = 8.8542*10**-12 #  C^2 * s^2 * kg^-1 * m^-3
h = 6.6261*10**-34 #  J

n = 20

E = [-((m_e*e**4)/(8*ep_0**2*h**2))*(1/n**2) for i in range(n+1)]

for i in range(n+1):
    print('Energy level for n = %g: %.2e' %(i, E[i]))

print('--------------------------------------------------------------------------')
print('i/f  f=1 \tf=2 \t\t f=3 \t\t f=4 \t\t f=5')
for i in range(1,6):
    print(str(i) + ': ', end='')
    for j in range(1,6):
        deltaE = -((m_e*e**4)/(8*ep_0**2*h**2))*(1/i**2 - 1/j**2)
        print('%.2e, ' %(deltaE), end='\t')
    print()
print('--------------------------------------------------------------------------')