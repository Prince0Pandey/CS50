'''try:
    x = int(input("what's x? "))
    #print(f"x is {x}")                 # NOTE: we should not include more line of code in try block

except ValueError:
    print("x is not integer")

else:
    print(f"x is {x}")                  # except & else blocks are mutually exclusive(only one executes)
'''

'''NOTE: this happens only when 'print(f"x is {x}")' statement is there without else block
   nameError: name 'x' is not defined because on line 2 x haven't assigned any value
   i.e when x taking input(it can take any value in string format) but when int
   function try to convert it into integer throws error and does not assign value to x
'''

'''
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not integer")
    else:
        break
        
print(f"x is {x}")
'''

'''
while True:
    try:
        x = int(input("what's x? "))
        break

    except ValueError:
        print("x is not integer")
print(f"x is {x}")
'''

'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))

        except ValueError:
            print("x is not integer")

        else:
            break          #after breaking we are returning value to function then why not return value instead of break
    return x
main()
'''

'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))

        except ValueError:
            print("x is not integer")

        else:
            return x
main()
'''

'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))

        except ValueError:
            #print("x is not an integer")        #instead of printing we can use 'pass' which will not do anything.
            pass                                 #pass: when we don't want to add any functionality to function
main()
'''

#In this program we had made get_int() function more usable by coder b/c coder can ask any think that he likes
def main():
    x = get_int("what's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()