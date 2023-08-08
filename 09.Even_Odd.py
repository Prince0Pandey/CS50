# n = int(input("enter number: "))
# if n%2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    n = int(input("enter number: "))
    if is_even(n):
        print("Even")
    else:
        print("Odd")

def is_even(x):
    '''if x%2 == 0:
        return True
    else:
        return False
'''
    '''return True if x%2 == 0 else False          # same as above'''
    return x%2 == 0
main()