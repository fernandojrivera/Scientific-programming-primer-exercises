print('----------------------') # table heading
print('    F     C     C^') # table heading
F = 0 # start value for F
dF = 10 # increment of F in loop
while F <= 100: # loop heading with condition
    C = (F - 32)*(5.0/9) # calculate the corresponding C for each F
    C_hat = (F - 30)/2
    print('%5.1f, %5.1f, %5.1f' %(F,C,C_hat)) 
    F = F + dF # increment F
print('----------------------') # end of table line (after loop)

'''
Trial run:
Expected result:
----------------------
    F     C     C^
  0.0, -17.8, -15.0
 10.0, -12.2, -10.0
 20.0,  -6.7,  -5.0
 30.0,  -1.1,   0.0
 40.0,   4.4,   5.0
 50.0,  10.0,  10.0
 60.0,  15.6,  15.0
 70.0,  21.1,  20.0
 80.0,  26.7,  25.0
 90.0,  32.2,  30.0
100.0,  37.8,  35.0
----------------------

>python3 f2c_table_while.py
----------------------
    F     C     C^
  0.0, -17.8, -15.0
 10.0, -12.2, -10.0
 20.0,  -6.7,  -5.0
 30.0,  -1.1,   0.0
 40.0,   4.4,   5.0
 50.0,  10.0,  10.0
 60.0,  15.6,  15.0
 70.0,  21.1,  20.0
 80.0,  26.7,  25.0
 90.0,  32.2,  30.0
100.0,  37.8,  35.0
----------------------

'''