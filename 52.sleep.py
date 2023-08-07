# def main():  
#     n = int(input("what's n? "))
#     for s in sheep(n):
#         print(s)
        
# def sheep(num:int) -> list:
#     flock = []
#     for i in range(num):
#         flock.append("🐑" * i)
#     return flock
        
# if __name__ == "__main__":
#     main()

    
#       Generators     #
def main():  
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)
        
def sheep(num:int) -> str:
    for i in range(num):
        yield "🐑" * i
        '''yield gives the value in parts(row of sheep) to {for s in sheep(n)} on line 19
        yield is returning iterator to main for iteration on line 19
        yield will do 1 iteration and hand the results to main then 2 iteration,...
        python suspend the function for while and remembers the state(iteration) then 
        next time start from where he left'''
        
if __name__ == "__main__":
    main()