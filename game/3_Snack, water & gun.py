# Gun_snack_Water game!!
# condition are:
# gun beat snack
# water beat gun
# sanck beat water
# 
# if gun win then win = -1 
# if snack win then win = 0
# if water win then win = 1 
# 
# #

import random

def check(player,computer):
    # gun beat snack return -1
    if player is not computer:
        if (player == -1 and computer == 0) or (player == 0 and computer == -1) : return -1   # -1 mean gun win
        elif (player == 1 and computer == -1) or (player == -1 and computer == 1) : return 1  # 1 mean water win 
        elif (player == 0 and computer == 1) or (player == 1 and computer == 0) : return 0   # 0 mean snack win
    else: return -10    # if draw return -10
    
def avg_win(player_win_count,computer_win_count,draw_count):
    if player_win_count > computer_win_count: return -5
    elif computer_win_count > player_win_count: return -6
    elif computer_win_count is player_win_count: return -7
    
print("Maximum time winner will be final winner!!!")
play_time = int(input("Enter how many time you want to paly : "))
print(("Now -->\nEnter -1 for Gun\nEnter 0 for Snack\nEnter 1 for Water"))
print("----------------------------")

player_win_count = 0
computer_win_count = 0
draw_count = 0
for i in range(0,play_time):
    player = int(input("You choose : "))
    computer = random.randint(-1,1)
    print(f"Com choose : {computer}")
    win = check(player,computer)
    
    if player is win: 
        print("Player win this round")
        player_win_count += 1
        print("----------------------------")
    elif computer is win: 
        print("Computer win this round")
        computer_win_count += 1
        print("----------------------------")
    else : 
        print("This round is draw!!")
        draw_count += 1
        print("----------------------------")

finall_win = avg_win(player_win_count,computer_win_count,draw_count)
if finall_win == -5: print("Final winner is YOU")
elif finall_win == -6: print("Final winner is Computer")
else:print("Final result is Draw")
    
    
    


