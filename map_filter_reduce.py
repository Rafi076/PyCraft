# in python, the map,filter and reduce function are builtin function that allow you to apply a fuction 
# to a sequence of element and returbn a new sequence. 
# these function are known as higher-order function, as they take other function as arguments.
# 
# 
# The map function applies a function to each elemnet in a sequence and return a new sequence  containing  the transformed elements.
# The map function has the following syntax: map(function, iterable) #

# here we create a list and cube the elemnet of list in map and convert it againg in list

# MAP:
#cube = lambda x: x*x*x

l = [3,1,9,4,6,2]
#cube_of_item = []
# for item in l:
#     cube_of_item.append(cube(item))
    
# #print(cube_of_item) # [27, 1, 729, 64, 216, 8] --> type is in map, to convet in list:
# cube_of_item = list(map(cube,l))
# print(cube_of_item) # [27, 1, 729, 64, 216, 8]


# FILTER :  syntax --> filter(predicate, iterable)
# filter_fun = lambda a: a>4
# newitem = []
# newitem = list(filter(filter_fun,l))
# #or  : not creating any function
# # newitem = list(filter(lamda a: a>4 ,l))#
# print(newitem) # [9, 6]



# REDUCE : syntax --> reduce(function, iterable)
# to sum the item on the givn list
from functools import reduce
sum = reduce((lambda x,y: x+y),l)
print(sum) # 25


