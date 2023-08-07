def main():
    x = int(input("enter value of x: "))
    print(f"{x} squared is {square(x)}")

def square(n):
    return n*n
'''return n**2         => means n square
    return pow(n,2)     => n is number and 2 means power of number
'''
main()