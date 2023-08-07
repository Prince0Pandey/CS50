# def total(galleons:int = 0, sickles:int = 0, knuts:int = 0):
#     return (galleons * 17 + sickles) * 29 + knuts

# # print(total(100,50,25), "knuts")

# coins = [100,50,25]

# # print(total(coins[0], coins[1], coins[2]), "knuts")

# print(total(*coins), "knuts")       
'''
star before variables means it will unpack the list & gives single value at a time without 
using comma as we use to separate (galleons, sickles, knuts).
total(*coins) == total(coins[0], coins[1], coins[2])
'''


# def total(galleons:int = 0, sickles:int = 0, knuts:int = 0):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons":100, "sickles":50, "knuts":25}

# # print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")

# print(total(**coins), "knuts")
'''
when we use dictionary we have to give double star/astersk before variable to unpack it, 
but in dictionary it will unpack with (key = pair) example: 'galleons = 100' along with comma 
if more key-value pairs present
total(**coins) == total(galleons = 100, sickles = 50, knuts = 25)
'''


'''
*args: function can take variable number of positional arguments
**kwargs: function can take variable number of keyword arguments(named parameter)
NOTE: We can write anything instead of args or kwargs, it is just a naming convention 
recommended by python
NOTE: args is list
NOTE: kwargs is a dictionary
'''
def f(*args, **kwargs):
    # print("Positional: ", args)
    print("Named: ", kwargs)

f(galleons = 100, sickles = 50, knuts = 25)