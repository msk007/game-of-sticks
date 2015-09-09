import random

def main():
    print("welcome to game of sticks!!!!!!!")
    stcks= sticknum()

    opponent=input("Would uou like to play against player 2 or the computer? Press 1 for computer or 2 for player 2: ")
        if input =='1':
    opponent=computer
        if input =='2':
    opponent=player2

sticks_left=int(0)
def sticknum():
    while opponent=='2' and opponent=='1':
        sticks=input("What is the number of sticky you want to start with? (10-100) ")
        if sticks >=10 and sticks<=100:
            print ("there are {} sticks in the pile." ).format(sticks)
        if sticks<10 or sticks>100:
            print "Number of sticks must be between 10 and 100."

opponent='1'
    while True:#human vs ai
        print ("there are {} sticks in the pile." ).format(sticks)
    sticks -= sticks_out(cur_player)
    if is_game_over(sticks):
        break
    if opponent==1:
        opponent=2
    else:
        opponent=1
print "You loose"



        break

print "Sticks left: " , sticknum
sticks_taken =int(input("Take how many sticks(1-3):"))
if sticks_taken >=3 or sticks_taken <1:
    print "Must choose 1-3"


    if sticks == 1:
        print "You loose"

def computer():
    ai=computer
    computer=int(0)
    while opponent=='1' and sticks>=2:
        playerstr==input("Player 1, enter the number of sticks to take: (1-3) -->")
        player1=int(player1str)
        if player>=1 and player<=3:
            print("Player 1 took {} sticks.").format(sticks)
            sticks-=player1
            print("There are {} sticks left in the pile.").format(sticks)
    computer==random.randint(1,3)
    print("computer took {} sticks").format(sticks_taken)
    sticks-=ai
    if sticks==1:
        print "you win!"
