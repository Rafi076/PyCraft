#In Python, __init__ is a special method known as the constructor. 
# It is automatically called when a new instance of a class is created. 
# The primary purpose of the __init__ method is to 
# initialize the attributes of the newly created object.#
class MyClass:
    def __init__(self, arg1, arg2):
        self.attribute1 = arg1
        self.attribute2 = arg2

# Creating an instance of MyClass
obj = MyClass("value1", "value2")

# Accessing attributes of the object
print(obj.attribute1)  # Output: value1
print(obj.attribute2)  # Output: value2
