x = float(input("enter value of x "))
y = float(input("enter value of y "))

'''
#round(number[,ndigits])
z = round(x + y)                        #round to nearest digit
print(f"{z:,}")                         #this will add comma after every 3 digits
'''
z = x/y

print(round(z,2))
'''this will round the number to 2 digit after decimal
    ex. x = 2, y = 3
        x/y should give 0.67
'''

print(f"{z:.2f}")                   # another way of rounding off to second place after digit