balance = 0     # balance is a global variable (by definition of global variable it can be read
# from any function but cannot change the value from any function )

def main():
    # balance = 0   here 'balance' is a local variable & can be accessed by main()
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)
    
def deposit(n):
    global balance
    balance += n        #here we are trying to change global variable but it thows error if we 
    # don't use global keyword inside a function
    
def withdraw(n):
    global balance      # this tells python that on next line 'balance' is not a local varaible 
    # using global we can change the value of balance
    balance -= n
    
if __name__ == "__main__":
    main()