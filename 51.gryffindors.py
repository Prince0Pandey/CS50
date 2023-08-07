# students = ["Hermione", "Harry", "Ron"]
# gryffindors = []

# for student in students:
#     gryffindors.append({"Name": student, "House": "Gryffindors"})

# print(gryffindors)


# students = ["Hermione", "Harry", "Ron"]
# gryffindors = [{"Name": student, "House": "Gryffindor"} for student in students]
# print(gryffindors)


#       DICTIONARY COMPREHENSION       #

# students = ["Hermione", "Harry", "Ron"]
# gryffindors = {student: "Gryffindor" for student in students}
# print(gryffindors)


#       Enumerate      #
students = ["Hermione", "Harry", "Ron"]
# for i, student in enumerate(students):
#     print(i+1,student)

for i, student in enumerate(students, start = 1):
    print(i,student)