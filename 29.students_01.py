# with open("students.csv") as file:
#     for line in sorted(file):
#         # row = line.rstrip().split(",")        #here row is a list which contains both name & bldg
#         # print(f"{row[0]} lives in {row[1]} Building")
#         name,building  = line.rstrip().split(",")
#         print(f"{name} lives in {building} building")


'''same as above but this time we append whole print statement in a list and using for loop 
to print it in sorted manner'''
# students = []
# with open("28.students.csv") as file:
#     for line in file:
#         name,building = line.rstrip().split(",")
#         students.append(f"{name} lives in {building} building")

# for student in sorted(students):    #sorted will sort the whole lines and by default it sorts 
#                                     #from left to right so it will give in ascending order
#     print(student)
    
  
# students = []
# with open("28.students.csv") as file:
#     for line in file:
#         name,building = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["home"] = building
#         student = {"name" : name, "building" : building}
#         students.append(student)

# # def get_name(x):
# #     return x["name"]
# # def get_house(student):       #here student is just a parameter
# #     return student["building"]
# # for student in sorted(students,key = get_name, reverse=True):#instead of get_name we can put get_house
# #     print(f"{student['name']} lives in {student['building']} building")

# #same as above but using lambda function
# for student in sorted(students,key = lambda stud:stud["name"], reverse=True):
# #lambda is used when we have to use it only once therefore it doesn't have any name(like get_name)
# #it takes parameter
#     print(f"{student['name']} lives in {student['building']} building")


#in upper codes there is a problem that we put(i.e prerana,apartment) when reading a CSV file python
#will split the first line based on "," so we get 3 values but we have only two values. 
# "prerana,apartment" are single value which require comma in it

# import csv
# students = []
# with open("28.students.csv") as file:
#     reader = csv.reader(file)
#     # for row in reader:
#     #     students.append({"name":row[0],"building":row[1]})
#     for name,home in reader:
#         students.append({"name":name,"building":home})

# for student in sorted(students,key=lambda std: std["name"]):   #here std is a parameter to lambda fun
#     print(f"{student['name']} is from {student['building']}")


import csv
students = []
with open("28.students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # students.append({"name":row["name"], "building":row["home"]})
        students.append(row)

for student in sorted(students,key=lambda std: std["name"]):   #here std is a parameter to lambda fun
    print(f"{student['name']} is from {student['building']}")