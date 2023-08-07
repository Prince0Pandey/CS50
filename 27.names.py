#In this program when we run and give input and rerun the file previous input data will be lost that's where
#file I/O is used

# names = []
# for _ in range(3):
#     names.append(input("what's your name? "))
#
# for name in sorted(names):
#     print(f"hello, {name}")


# name = input("what's your name? ")
# file = open("names.txt","a") # "a" = append at the end     "w" = rewrite everytime we run our program
# file.write(f"{name}\n")
# file.close()                 #sometimes we forget to close the file & it may or may not cause problem


#name = input("what's your name? ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")


'''we first store the line then print it using for loop'''
# with open("names.txt","r") as file:
#     lines = file.readlines()

# for line in lines:
#     # print("hello,",line)        #it will print but leaving 1 line gap because when we append 
#                                 #the names with \n it will print next line
#     print("hello,",line.rstrip())


'''we don't need to first store the line then print it using for loop, we can directly print lines'''
# with open("names.txt","r") as file:
#     for i in file:
#         print("hello,",i.rstrip())


'''now i want to print each line in alphabetical order'''
# names = []
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
#
# for name in sorted(names):
#     print("hello,",name)


'''same as above but in simply code'''
with open("names.txt") as file:
    for line in sorted(file,reverse=True):
        print("hello,",line.rstrip())