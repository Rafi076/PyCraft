# When a class inherit from a parent class, it can override or extend
# the method defined in the parent class. #

class parentclass:
    def parentFunction(self):
        print(f"This is parent class\nHere the attribute is = im {self.name} and {self.age} year old.")

class childclass(parentclass):
    def childFunction(self,name,age,work):
        self.work = work
        self.name = name
        self.age = age
        super().parentFunction()
        print(f"Currently working with {self.work}.")

callObject = childclass()
callObject.childFunction("Rafi",24,"google")


#Method Overriding:-->
class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self): #This function is just to multiply two element
        return self.x * self.y

# create a class for circle to override shape calss:
class circle(shape):
    def __init__(self,radious):
        self.radious = radious
        super().__init__(radious,radious)
    
    # create a class for multipling radious^2 with 3.14
    def circleArea(self):
        return 3.1416 * super().area() 

result = circle(5)
print("Area of circle = ",result.circleArea()) # Area of circle =  78.53999999999999


