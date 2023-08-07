# import random

# class Hat():
#     def __init__(self):
#         self.houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    
#     def sort(self,name):
#         print(name, "is in", random.choice(self.houses))
# hat = Hat()
# hat.sort("harry")


import random

class Hat():

    houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
    # 'houses' is a class variable & can be used by other methods inside of class
    
    @classmethod
    def sort(cls,name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("harry")