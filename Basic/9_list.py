# to find the specific item from the list 
# color = ["green","red","white","blue","black","purpale"]
# for i in range(len(color)):
#     if(color[i]=="red"): 
#         print(color[i],"found at index ",i)
#     else: 
#         print("Good to go!!")
        
        

# to find the specific item from the list 
# color = ["green","red","white","blue","black","purpale"]
# for i in range(len(color)):
#     if "bg" in color: 
#         print(color[i],"found at index ",i)
#     else: 
#         print("Good to go!!")
        

# color1 = ["green","red","white","blue","black","purpale"]
# if "yallow" in color1: print("Yes")
# else:print("No")

# print(color1[1:4],end=' ') # ['red', 'white', 'blue'] 
# print(color1[0:6:2],end=' ') # ['green', 'white', 'black']

# # to add in list
# color1.append("pink")
# print(color1,end=' ') # ['green', 'red', 'white', 'blue', 'black', 'purpale', 'pink']

# alist = [11,12,3,2,33,4,6,21,5]
# alist.sort()
# print(alist,end='') # [2, 3, 4, 5, 6, 11, 12, 21, 33]
# alist.reverse()
# print(alist,end='') # [33, 21, 12, 11, 6, 5, 4, 3, 2]
# print(alist.index(6),end='') # 4

# district = ["dhaka","chittagong","khulna"]
# new = ["syllhat","rangpur","Barishal"]
# district = new.copy()
# print(district) # ['syllht', 'rangpur', 'Barishal']

# # to insert chittagong between syllhat and rangpur
# district.insert(1,"chittagong") 
# print(district) # ['syllhat', 'chittagong', 'rangpur', 'Barishal']

# # to extend list
# district1 = ["dhaka","chittagong","khulna"]
# new1 = ["syllhat","rangpur","Barishal"]
# district1.extend(new1)
# print(district1) # ['dhaka', 'chittagong', 'khulna', 'syllhat', 'rangpur', 'Barishal'] 


# ## KBC game ##

# quetions = [
#     ["Which language was used to create fb ?","Python","JS","php","None",1],
#     ["What is the capital of Bangladesh ?","Chittagon","khulna","Dhaka","syllhat",2],
#     ["What is the addition of 1+1 = ?","01","1","2","10",3]
# ]
# levels = [1000,2000,3000,4000,5000,6000,7000,8000]
# money = 0
# for i in range(0,len(quetions)):
#     quetion = quetions[i]
#     print(f"\nQuetion for tk.{levels[i]}")
#     print(f"Q:{quetion[0]}")
#     print(f"a.{quetion[1]}     b.{quetion[2]}")
#     print(f"c.{quetion[3]}       d.{quetion[4]}")
#     replay = int(input("Enter your answer (1-4): "))
#     if(replay == quetion[-1]):
#         print(f"Correct answer! you won tk- {levels[i]}")
#         if(levels == 4): 
#             money = 3000
#         elif(levels == 6): 
#             money = 4000
#     else:
#         print("wrong answer!")
#         break