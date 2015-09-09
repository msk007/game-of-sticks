

def main():
    print("welcome to game of sticks!!!!!!!")
    sticks= get_stick_num()
    sticks_taken =int(input("Take how many sticks(1-3):")

    while True
        print ("there are {} sticks in the pile." ).format(sticks)
        if is_game_over(sticks):

        break
        if opponent==1:
            opponent=2
        else:
            opponent=1
            print "You loose"

        break


def is_game_over(stick_num):
    if stick_num<=0:
        return True
    else:


def sticknum():
    sticks=input("What is the number of sticky you want to start with? (10-100) ")
        if sticks >=10 and sticks<=100:
            print ("there are {} sticks in the pile." ).format(sticks)
        if sticks<10 or sticks>100:
            print "Number of sticks must be between 10 and 100."





        break

print "Sticks left: " , sticknum
sticks_taken =int(input("Take how many sticks(1-3):"))
if sticks_taken >=3 or sticks_taken <1:
    print "Must choose 1-3"


    if sticks == 1:
        print "You loose"

opponent='2
while True:'
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
    print("Opponent took {} sticks").format(sticks_taken)
    sticks-=ai
    if sticks==1:
        print "you win!"
