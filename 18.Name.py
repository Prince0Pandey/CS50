import sys
# try:
#     print("Hello, my name is",sys.argv[1])
# except IndexError:
#     print("Very Few Arguments")


# We can use if else instead of try & except block as it is not required everytime to use except

# if len(sys.argv) < 2:
#     print("Very Few Argument")
# elif len(sys.argv) > 2:
#     print("too many Argument")
#
# else:
#     print("Hello, my name is", sys.argv[1])

# Instead of printing first name we can print any thing but it should be inside the string " "
# when we run this program in python


# if len(sys.argv) < 2:
#     sys.exit("Very Few Argument")
# elif len(sys.argv) > 2:
#     sys.exit("too many Argument")
#
# print("Hello, my name is", sys.argv[1])     # if we haven't used sys.exit this line will execute independent of any input


if len(sys.argv) < 2:
    sys.exit("Very Few Argument")
for arg in sys.argv[1:-1]:
    print("Hello, my name is",arg)