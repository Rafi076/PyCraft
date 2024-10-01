class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def Show_details(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed
        
    def Show_details(self):
        Animal.Show_details(self)
        print(f"Breed : {self.breed}")
        
class Golden_Retriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name, breed = "Golden Retriever")
        self.color = color
        
    def Show_details(self):
        Dog.Show_details(self)
        print(f"Color : {self.color}")

o = Golden_Retriever("Tommy","Brown")
o.Show_details()
        