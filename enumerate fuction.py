# enumerate fuction is a builtin function in python that allows you
# to loop over a sequence (such as list,tuple,string) and get the index value of each element in the sequence at the same time
# here a basic example of how it works:#
# here we will get index and value at the same time
marks = [78,72,70,88,98,87,91,78]
for index,mark in enumerate(marks):
    print(index,mark)
    if(index == 4):
        print("rafi, is awesome!!")