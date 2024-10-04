# The self parameter is a reference to the current instance of the class, and is 
# used to access variables that belong to the class.#

# class Details:
#     name = "Rafi"
#     age = 24
    
#     def desc(self):
#         print("My name is", self.name,"and i'm",self.age,"year old.")
        
# obj1 = Details()
# obj1.desc()

#Another example:
# class person:
#     # we dont need to declear extra variable as java while creating class in python.#
#     def info(self): print(f"{self.name} is a {self.occupation}. his networth is {self.networth}.")
    
# person1 = person()
# person1.name = "Rafi"
# person1.occupation = "software engineer"
# person1.networth = 100
# person1.info()

# person2 = person()
# person2.name = "Raisa"
# person2.occupation = "App developer"
# person2.networth = 100
# person2.info()



# CONSTRACTOR :-->
# A constractor is a special method in a class used to create and initializa an object of a class.
# it's unic function that get called autometically when an object is creatde of a class. The main purpose ofs constractor is 
# to initialize or assing values to the data member of that class.it cannot return any vvalue other than none. syntax: def __init__(self): #
class person:
    
    def __init__(self,nm,occ):
        self.name = nm      # CONSTRACTOR
        self.occpation = occ    # CONSTRACTOR
    def info(self):
        print(f"{self.name} is a {self.occpation}")
        
a = person("Rafi","SE")
a.info()
b = person("Raisa","AD")
b.info()