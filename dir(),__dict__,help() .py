#This method make it easly to us to understand how clas rsolve functiion andexcecute code.and
# dir()
# it return a list of all atribute and method availabel for an objec.it is a usefuk tool for discovering what you csn do with an object
# example:-->#
x = [2,1,9]
print(dir(x))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', 
#  '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
#  '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
#  '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', 
#  '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
#  'clear', 'copy', 'count', 'extend', 'index', 
#  'insert', 'pop', 'remove', 'reverse', 'sort']


# The __dict__ attribute return a dictionary representation of an object attribute. it is a useful tool for introspection
# example:-->#

class person:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
        
per = person("rafi",24,"221003712")
print(per.__dict__) # {'name': 'rafi', 'age': 24, 'id': '221003712'}

#The help() function is used to get help documentation for an object,
# including a description if its attribute and method.it tells everything about a call/function..
# example:-->
class Engineer:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
        
per = Engineer("rafi",24,"221003712")
print(per.__dict__)
print(help(Engineer))