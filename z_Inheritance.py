class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname

    def Full_name(self):
        print(self.first_name,self.last_name)

# name = Person("Prince","pandey")
# name.Full_name()

class Student(Person):
  pass

x = Student("ratnesh", "pandey")
x.Full_name()

