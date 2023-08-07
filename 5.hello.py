'''def hello(x = "Everyone"):           # if no arguments passed by default it will print 'everyone'
    print(f"Hello, {x}")

name1 = input("enter your name: ")
hello(name1)
hello()'''                             # here no arguments are passed so it will print 'hello everyone'

'''NOTE: in above program we first have to define a function then only we can use it
         but if we call it first and define later it will throw an error
         for this problem we can use "main()" given below
'''
def main():
    name = input("enter your name: ")
    hello(name)

def hello(x = "everyone"):
    print("hello,",x)

main()