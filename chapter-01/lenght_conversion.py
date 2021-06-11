input = 640
inch = (100)*(1/2.54) # m to in
feet = inch*(1/12) # in to ft
yard = feet*(1/3) # ft to yd
mile = yard*(1/1760) # yd to mi

print('''original lenght in meters = %g m
inches = %g in
feet = %g ft
yards = %.2f yd
miles = %.2f mi''' %
(input, inch*input, feet*input, yard*input, mile*input))

'''
Trial run:
Expected result:
original lenght in meters = 640 m
inches = 25196.9 in
feet = 2099.74 ft
yards = 699.91 yd
miles = 0.40 mi
>python3 lenght_conversion.py
original lenght in meters = 640 m
inches = 25196.9 in
feet = 2099.74 ft
yards = 699.91 yd
miles = 0.40 mi
'''