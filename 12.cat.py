def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("enter a number: "))
        if n > 0:
            break           # instead of break here we can replace it by 'return n' that will return n and break
    return n


main()