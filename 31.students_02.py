import csv

name = input("what's your name? ")
home = input("where's your name? ")

with open("30.students_02.csv","a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name,home])
    writer = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"home": home, "name": name})