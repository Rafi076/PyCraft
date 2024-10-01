# in python, a lambda function is a small anonymous functin without a name.
# is defined using the lamda keyword and the following syntax: lamda arguments: expression
# #

def appl(fx,value):
    return 6+fx(value)

# basicali we create a function like this =>#
# def double(x):
#     return x*2

# BUT we can write it by this way too --># 
double = lambda x: x*2
print(double(5))

cube = lambda c: c*c*c
print(cube(3))

avg = lambda x,y:  (x+y)/2
print(avg(3,5))



print(appl(cube,2)) # 14
# or
print(appl(lambda c: c*c*c,2)) # 14

