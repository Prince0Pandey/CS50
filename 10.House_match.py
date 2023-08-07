name = input("what's your name: ")
'''
if name == "harry":
    print("gryffindor")
elif name == "hermione":
    print("gryffindor")
elif name == "ron":
    print("gryffindor")
elif name == "draco":
    print("slytherin")
else:
    print("who ?")
'''

'''
if name == "harry" or name == "hermione" or name == "ron":
    print("Gryffindor House")
elif name == "draco":
    print("Slytherin House")
else:
    print("Who ?")
'''

'''
match name:
    case "harry":
        print("Gryffindor House")
    case "hermione":
        print("Gryffindor House")
    case "ron":
        print("Gryffindor House")
    case "draco":
        print("Slytherin House")
    case _:
        print("Who ?")
'''

match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor House")
    case "draco":
        print("Slytherin House")
    case _:
        print("Who ?")
