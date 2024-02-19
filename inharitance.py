# when a class derives from another calss.
# the chiled class will inherit all the public an protected proparticess and
# methods from the parent calss. in addition, it can have its own proparties and 
# method, this is called as inheritance.
# syntax:
# class basesclass:
#   body of baseclass;
# class childclass(baseclass):
#   body of childclass;
# #

# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def details(self):
#         print(f"The name of employee {self.name} & the ID is {self.id}.")
        
# class programmer(Employee):
#     def Language(self):
#         print("Default language is pyton.")
        
        
# Employee = int(input("Enter the number of employee : "))
# for i in range(0,Employee):
#     name = input("Enter the name of Employee : ")
#     id = int(input("Enter the id of Employee : "))

#     person = programmer(name,id)
#     person.details()
#     person.Language()
    
    
# Access modifer 3type : 

####********* 1) Public--> we used up.where member of a  class can be accessed from outside.That mean we can accessed name and id from out side of Employee calss.

####********* 2) privet--> here we can not access a privet member of a class from out side. lets create a privet variabl named as id (we write : self.__id = id )
# But we can asccess it by another way : #
# class employee:
#     def __init__(self) :
#         self.__name = "Rafii" # name created as protected mood

# MyObject = employee()
# #print(MyObject.__name)  # can not be accessed directly

# print(MyObject._employee__name) #can be accessed indirectly



####********* 3) Protected --> it's used to describe a member of a class that is intended to be accessed by calss it self and it sub class
# lets create a protceted variabl named as id (we write : self._id = id ).
 