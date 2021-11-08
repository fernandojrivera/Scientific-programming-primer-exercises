print('--------------') # table heading
print('    F     C') # table heading
F = 0 # start value for F
dF = 10 # increment of F in loop
while F <= 100: # loop heading with condition
    C = (F - 32)*(5.0/9) # calculate the corresponding C for each F
    print('%5.1f, %5.1f' %(F,C)) 
    F = F + dF # increment F
print('--------------') # end of table line (after loop)

'''
Trial run:
Expected result:
--------------
    F     C
  0.0,   -17.8
  0.0,  -12.21
   .      .
   .      .
   .      .
  90.0,  32.2
 100.0,  37.8
--------------
>python3 f2c_table_while.py
--------------
    F     C
  0.0,   -17.8
  0.0,  -12.21
   .      .
   .      .
   .      .
  90.0,  32.2
 100.0,  37.8
--------------
'''