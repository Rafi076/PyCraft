# Whenever string literals are present just after the definition of a function,
# module, class or method, they are associated with the object their doc-attribute.
# we can later use this attribute to retrieve this docstring.
name = "Rafi"
age = 24
prices = 2.56754
txt = f"Hello im {name}. im {age} year old.Today's meat prices is {prices:.3f}"
print(txt)



def square(n):
    '''Take a number n, returns the number of n''' 
    print(n**2)
   
square(5)
print(square.__doc__)  # Take a number n, returns the number of n  
    
# PEP 8:
# it stand for python Enhancement Proposal. it is a document that provide guidlines and best
# practices on hoe to write python code.
    