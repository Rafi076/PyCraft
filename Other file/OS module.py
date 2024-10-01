#The os module in python is a built in library that provides function for interacting with the operating system
# it allows you to perfome a wide varity of task, such as regarding and writing
# files, interacting with file sysytem, and running sysytem commands#

#lets create a folder name "rafis_1_to_100_days" inside this folder create more 100 file named day1 to day100 #
import os
# if(not os.path.exists("rafis_1_to_100_days")):
#      os.mkdir("rafis_1_to_100_days")
    
# for i in range(0,100):
#     os.mkdir(f"rafis_1_to_100_days/day{i+1}") # --> 100 file created inside 
   
   # to rename every file as Chalnges1 to chalnges100: 
# for i in range(0,100):
#     os.rename(f"rafis_1_to_100_days/day{i+1}",f"rafis_1_to_100_days/chalange{i+1}") # --> 100 file renamed as chalnge1 to chalang100
                # sources ,                    # destination
                
                
# to see file list inside a folder:
file = os.listdir("rafis_1_to_100_days")
print(file)

#To see what inside a file:
for task in file:
    print(task)
    print(os.listdir(f"rafis_1_to_100_days/{task}"))
    #['today_task.md']
    # chalange40 #
 
