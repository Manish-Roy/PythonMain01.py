#To import the random procedure
import random

#now moves for pc
moves=["rock","paper","scissors"]


#for an infinite loop:
play_again="true"



#Now looping the programme based on  the switch created:
while play_again == "true":


    #cmove is for computer to choose randomly and pmove for player or  user:
    cmove=random.choice(moves)
    pmove=input("Whats is your move: rock, paper or scissor")
    

    #the best possible outcome:
    if cmove==pmove:
        print("tie")


        #other outcomes can be:
    elif pmove=="rock" and cmove=="scissor":
            print("{Player wins")
    elif pmove=="rock" and cmove=="paper":
            print("Computer wins")
    elif pmove =="scissor" and cmove == "rock":
            print("Player wins")
    elif pmove== "paper" and cmove =="scissor":
            print("Computer wins")
    elif pmove=="scissor" and cmove =="paper":
            print("Player wins")
    elif pmove=="scissor" and cmove =="rock":
            print("Computer wins")
    elif pmove== "paper" and cmove =="rock":
            print("Player wins")