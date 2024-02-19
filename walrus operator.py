#warlus operatioon is a new addition to python 3.8 and allow you to assing a value to variable within an expression.
# this can be useful when we need to use a value multiple times in loop, but dont want to repeat the calcullation.
# its represented by the syntax (:=) and can be used in a varity of contexst including loop and if statement.#
#Example1:
# a = True
# print(a:=False) # here False assingd to 'a' and print False instand of true
#
# Example2:
number = [3,13,5,26,7]#
while(n:= len(number)) > 0:
    print(number.pop())
    
#Usally we do to take input#
    # foods = list()
    # while True:
    #     food = input("What food do you like?? : ")
    #     if food=="quite": break
    #     foods.append(food)
    
#But we can do this by this:--#
foods = list()
while (food := input("What food do you like?? : ")) != "quite":
    foods.append(food)