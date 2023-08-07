# name = input("Name: ")
# house = input("House:")
# print(f"{name} from {house}")


# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()
    
    
# def main():
#     #name, house = get_student()
#     #print(f"{name} from {house}")
    
#     student = get_student()  
#     print(f"{student[0]} from {student[1]}")
    
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     #return name, house              # here we are not returning 2 values, because 'return' only 
#                                     # return single value so if we specify 2 values seperated with
#                                     # comma then it returns tuple
#     #return (name,house)             #both the return statement are same
#     return [name, house]            # same as above but it is returning list i.e mutable       

# if __name__ == "__main__":
#     main()


# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")
    
# def get_student():
#     # student = {}
#     # student["name"] = input("Name: ")
#     # student["house"] = input("House: ")
#     # return student
    
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# if __name__ == "__main__":
#     main()
   
    
'''
Class is like a blueprint of house
Class is a definition of a datatype i.e Student
Object(instance of class) is when we use the blueprint for building a specific house
When we use class we create objects 
three dot's in class refer that we don't want to implement anything now
We can make our class mutable or immutable
Just by defining the class we get a function whose name is same as class
Classes comes with a method that you can define and they behave in a special way
By default any function inside a class will take atleast one parameter called self
We can make any parameter optional by typing 'house = None'
'raise' : it is used to raise our own exceptions in python
__str__ takes reference to the current object using self.
__str__ will get called automatically whenever we want to convert student object to a string
__str__ takes only one argument i.e self
decorators: function which modify the behaviour of other function
Getter(@property above the function): function in a class that gets some attribute
Setter(@house.setter): function in a class that sets some value, here 'house' is a name of a 
variable that is used to create setter function.
'''

# class Student:
#     def __init__(self, name, house):   #init method specifically known as instance method
#                             #this method is use to initialize the contents of a object from a class
#                             #by default __init_ takes reference to the current object using self
#         self.name = name.title()
#         self.house = house     #this line will call setter function and check the input.
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing Name!")
#         self._name = name
    
#     @property
#     def house(self):
#         return self._house
    
#     @house.setter
#     def house(self,house):
#         if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house
# # Above setter function will get called either when we create an object or when we modify the value of it
  
# def main():
#     student = get_student()
#     # print(f"{student.name} from {student.house}")
#     print(student)                  #it will give the location of object/address of object in memory
#                                     #but if we want to print the value inside of object we have to
#                                     #use '__str__' in our class.
    
# def get_student():
#     # student = Student()            #instantiating object name student or creating object of a class
#     # student.name = input("Name: ")
#     # student.house = input("House: ")
#     # return student    #attributes of object student are name, house also known as instance variable
    
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)         #here i am treating name of class as function and passing
#                                         #two values name & house
#                                         #this is also known as a constructor call/this is going to
#                                         #contruct a student object for me
# if __name__ == "__main__":
#     main()
    

# here we have created a get() inside of a class so that related functionality will be together
class Student:
    def __init__(self, name, house):
        self.name = name.title()
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)     # 'cls' is a refernce to class 'Student'
  
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()