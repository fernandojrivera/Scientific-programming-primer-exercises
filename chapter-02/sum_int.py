n = 10
s = 0
for i in range(1, n+1):
    s+=i
expected = n*(n + 1)/2
print('Sum: %g. The expected value was %g.' %(s,expected)) 

'''
Trial run:
Expected result:
Sum: 55. The expected value was 55.

>python3 sum_int.py
Sum: 55. The expected value was 55.
'''