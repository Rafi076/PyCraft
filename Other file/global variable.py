#To handal global variable inside the function# 
x = 10

def my_fun():
    global x 
    x = 5

my_fun()
print(x) # print 5 instend of 10
