# i made a simple game called Rock paper scissors. its called Rock paper scissors because the player picks rock, paper or scissors and the computer picks the same. the player wins if the player picks rock and the computer picks scissors, the player wins if the player picks paper and the computer picks rock, and the player wins if the player picks scissors and the computer picks paper. the player and the computer tie if they both pick the same. the player and the computer lose if they both pick the same.

import random
# Edit by Owen - 'fileinput' was unused, also you can specify imports on one line: "import beans1, beans2, beans3"

player = input("Enter Rock, Paper or Scissors: ")
def RockPaperScissors(player):
# List of RPS
        player = player.lower()
        rps_list = ["rock", "paper", "scissors"]
        playerwins = [["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"]] #combinations of where the player is winning 
        opponent = random.choice(rps_list) #opponent's choice
        if (player not in rps_list): #make sure the answer is valid
            print("Input is invalid")
            return RockPaperScissors(input("Enter Rock, Paper or Scissors: ")) #Edit by Jatin to make it loop
        print("The player picked " + player + " and the opponent picked " + opponent) #print what the player picked and the opponent did
        print(str(PlayerArt(player)) + str(OpponentArt(opponent)))
        if ([player, opponent] in playerwins):     #if the combination is in the winning list 
            print("The player wins!")
        elif(player == opponent): #if they are same 
            print("It's a tie!")
        else:                      # otherwise the opponent wins 
            print("The opponent wins!")
        return RockPaperScissors(input("Enter Rock, Paper or Scissors: ")) #Edit by Jatin to make it loop

def PlayerArt(player):
    if (player == "rock"):
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


    if (player == "paper"):
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


    if (player == "scissors"):
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """) 
    return ""

def OpponentArt(opponent):
    if (opponent == "rock"):
        print("""
     _______
    (____   '---   
   (_____)
   (_____)
    (____)
     (___)__.---
            """)

    if (opponent == "paper"):
        print("""
              _______
         ____(____   '---
        (______
        (_______
         (_______
           (__________.---
        """)    


    if (opponent == "scissors"):
        print("""
           _______
      ____(____   '---
     (______
    (__________
          (____)
          (___)__.---  
    """) 
    return ""

RockPaperScissors(player)

