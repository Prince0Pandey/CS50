'''     INHERITANCE     '''

class Wizard():
    def __init__(self,name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)      # this will inherit the properties of superclass 'Wizard'
        self.house = house
    ...
        
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...
        
wizard = Wizard("Albus")
student = Student("Harry","Gryffindor")
professor = Professor("Severus","Defense Against the Dark Arts")
...

#Operator Overloading: ex. + means addition but it can be used for concatenation of a string(overloaded)