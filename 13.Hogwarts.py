'''students = ['harry','hermione','ron']

# for student in students:
#     print(student)

 for i in range(len(students)):
     print(i+1,students[i])
'''
students = [
    {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell Terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=", ")