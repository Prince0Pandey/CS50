#     SET     #
students = [
    {"name": "Harmione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])

houses = set() #Defining empty set(set does not have duplicates but list have)lst = list() empty list

for student in students:
    houses.add(student["house"])        #Set does not have 'append' instead it has 'add' function
    
for house in sorted(houses):
    print(house)

# ps = {"gamora","str","greek",9,0,0}       # set
# print(ps)