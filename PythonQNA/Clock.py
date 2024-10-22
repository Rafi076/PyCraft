# creating international clock:
import time
clock = time.strftime('%H:%M:%S')
print("Current Time : ", clock)
hour = int(time.strftime('%H')) # string should convert to intiger!!
#min = int(time.strftime('%M'))
if( 0 <= hour < 6):
    match hour:
        case 0: 
            string = "it is bed time"
            print(' '.join(char for char in string)) # to print in same line
            
        case _ if (1<= hour <= 4) : # used with condition
            string = "Dark mid night" 
            print(' '.join(char for char in string)) # used loop
            
        case _: print("Time to wake up") # case_: used as default
        
elif(6 <= hour < 11): 
    match hour:
        case 6: print("Wake up")
        case _ if (7<= hour <= 10) : print("Complite Breakfast") # used with condition
        case _: print("sun up!") # case_: used as default
        
elif(11 <= hour < 18): 
    match hour:
        case 11: print("After Noon Time")
        case 12 if (12<= hour < 18) : print("Lunch Time") # used with condition
        case _: print("sun Down!") # case_: used as default

elif(18 <= hour < 23): 
    match hour:
        case _ if (18 <= hour < 22):  # You can use an underscore (`_`) for the match if it's a range check
            print("Evening Time")
        case 22:  # You are specifically checking for hour 22 (10 PM)
            print("Dinner Time")
        case _: 
            print("Sun Down already!")  # Default case for anything outside the previous conditions


else: 
    match hour:
        case 18: print("After Noon Time")
        case _ if (19<= hour < 22) : print("Getting Night") # used with condition
        case _ if (22 <= hour <= 24):  # case_: used as default
            string = "Ending today soon"
            print(' '.join(char for char in string)) # used loop