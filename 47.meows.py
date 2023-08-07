# MEOWS = 3       
'''
it is just a naming convention in python through which you understand that it is
constant but there is no mechanism which will prevent me from changing it.
'''
# MEOWS = 4       #this will work fine and now value of 'MEOWS' updated to 4

# for _ in range(MEOWS):
#     print("meow")


# class Cat:
#     MEOWS = 3
    
#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")
            
# cat = Cat()
# cat.meow()


# def meow(n:int):       #TYPE HINT   #using mypy for checking of code before executing/running
#     for _ in range(n):
#         print("meow")

# number: int = int(input("enter number: "))
# meow(number)


'''
SAME AS ABOVE BUT THIS TIME INSTEAD OF PRINTING WE THINK THAT MEOW FUNCTION WILL RETURN SOME
STRING VALUE WHICH WILL THROOW ERROR
'''
# def meow(n:int) -> None:
#     for _ in range(n):
#         print("meow")

# number: int = int(input("enter number: "))
# meows: str = meow(number)       #this will call meow function & execute it then try to assign 
#                                 #return value to it
# print(meows)
'''this will return 'None' as 'meow()' does not explicitly return a value as
there is no return statement written in function,but by default if python explicitly does not
return a value then it's implicit return value is 'None'
'''

# def meow(n:int) -> str:
#     return "meow\n" * n

# number: int = int(input("enter number: "))
# meows: str = meow(number)
# print(meows, end = "")


# import sys

# if len(sys.argv) == 1:
#     print("meow")
    
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")

# else:
#     print("usage: meows.py")

import argparse

parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):     #args.n contain integer thatwe typed after "-n"
    print("meow")