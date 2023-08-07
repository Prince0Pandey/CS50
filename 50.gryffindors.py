# LIST COMPREHENSION
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

# gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
# print(sorted(gryffindors))


students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"}
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"
'''
above code is same as below code
def is_gryffindor(s):
    if s["house] == Gryffindor:
        return True
    else:
        return False
'''
gryffindors = filter(is_gryffindor, students)

# gryffindors = filter(lambda s: s["house"] == "Gryffindors", students)
# this above line of code contains the function itself using lambda

'''
filter(function, iterable): filter takes function which returns true or false, 
if true about the current student then it will include it to gryffindors
'''

for student in sorted(gryffindors, key = lambda s: s["name"]):
    #this will sort the dictionary on the basis of name using lambda function
    print(student["name"])