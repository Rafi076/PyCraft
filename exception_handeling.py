    ########### For else ##############
# here its loop with else topic!! 
# here else refer that loop is not breaked! it refer loop is end!!
for i in range(6):
    print(i,end=' ') # 0 1 2 3 4
    if i == 4: break
else: 
    print("sorry")
    
    ##### get the Differences ####
for i in range(6):
    print(i,end=' ') # 0 1 2 3 4 5
else: 
    print("sorry") # sorry
    
    
    #########Exception###############
### To handeling error in pyhton we use excepton ######
# Exception handeling is the process of responding to unwanted or unexpected events when a Pc program run #
# suppose you want to print a multiplication table by giving int type data
# but you gaved string type data at that time compiler shows error but to handel this error : --->>#
# let a input a
a = input("Enter a number : ") # a is a random input type
print(f"multiplication table of {a} is : ") # lets give a string type input
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e) # invalid literal for int() with base 10: 'r'

## rest of part of code will continue to execuit
print("Next part of code") # Next part of code

### We also use it to handel many other error ###
try:
    num = int(input("Enter a integer : "))
    a = [6,3,4,1,9]
    print(a[num])
except ValueError: 
    print("Number entered is not an integer!")
except IndexError:
    print("Index error!")
    
    
    
######## Finally #########
# Here finally keyword always execuit.so,it is genarally used for doing
# the concluding task like closing file or closing database resources or closing database connection
# or may be ending the program excecution with delightful message! #

try: 
    list = [1,3,5,8,4]
    index = int(input("Enter a index to print item : "))
    print(list[index])
except:
    print("Not Valid index!")
finally: 
    print("Im always execuit!")
    
## another example: ****important*****

def func():
    try: 
        list = [1,3,5,8,4]
        index = int(input("Enter a index to print item : "))
        print(f"{index} is at index = ",list[index]) 
        return 1
    except:
        print("Not Valid index!")
        return 0 
    finally: 
        print("Im always execuit!")

x = func()
print(x)
