import pandas as pd
pd.options.display.float_format = '{:g} g'.format

filename = 'densities.dat'
#various densities in g/cm^3
df = pd.read_table(filename, sep='\s{2,100}', names=['material','density'], engine='python', index_col='material')

#list of materials to compute
arr = ['iron','air', 'gasoline', 'ice', 'human body', 'silver', 'platinium']

#get the density of my list of materials
df_cut = df.loc[arr]

#populate a volume variable with 1 liter converted to cubic cm
volume = 1*(1000) #1 liter in cm^3

#calculate the mass of my list of materials
df_cut['mass']=volume*df_cut['density']
print(df_cut['mass'])

'''
Trial run:
Expected result:
material
iron          7800 g
air            1.2 g
.               .
.               .
>python3 1liter.py
material
iron          7800 g
air            1.2 g
.               .
.               .
'''