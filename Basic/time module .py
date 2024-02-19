#the time module in python provide a set of function to work with time related operation #
import time 
def whileloop():
    i=1
    while i<5000:
        print(i,end=' ')
        i+=1

def forloop():
    for i in range(5000):
        print(i,end=' ')

initwhile = time.time()
whileloop()
print("Time for while loop : ",time.time()-initwhile) # Time for while loop :  0.03490948677062988
print("\n")
time.sleep(10) # sleep for 10sec

initfor = time.time()
forloop()
print("Time for for loop : ",time.time()-initfor) # Time for for loop :  0.025932788848876953

print("The local time is : ")
current_time = time.localtime()
formatted_time = time.strftime("%d-%m-%Y %H:%M:%S",current_time) # to print current time
print(formatted_time)

        