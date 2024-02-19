## KBC game ##

quetions = [
    ["Which language was used to create fb ?","Python","JS","php","None",1],
    ["What is the capital of Bangladesh ?","Chittagon","khulna","Dhaka","syllhat",2],
    ["What is the addition of 1+1 = ?","01","1","2","10",3]
]
levels = [1000,2000,3000,4000,5000,6000,7000,8000]
money = 0
for i in range(0,len(quetions)):
    quetion = quetions[i]
    print(f"\nQuetion for tk.{levels[i]}")
    print(f"Q:{quetion[0]}")
    print(f"a.{quetion[1]}     b.{quetion[2]}")
    print(f"c.{quetion[3]}       d.{quetion[4]}")
    replay = int(input("Enter your answer (1-4): "))
    if(replay == quetion[-1]):
        print(f"Correct answer! you won tk- {levels[i]}")
        if(levels == 4): 
            money = 3000
        elif(levels == 6): 
            money = 4000
    else:
        print("wrong answer!")
        break