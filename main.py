import random

#Taking in user's choice
user_actn = input("\nEnter a choice (1 for Rock, 2 for Paper, 3 for Scissors, 4 for Lizard, 5 for Spock):-\n")
if user_actn == "1":
    choice = "Rock"
elif user_actn == "2":
    choice = "Paper"
elif user_actn =="3":
    choice = "Scissors"
elif user_actn == "4":
    choice = "Lizard"
elif user_actn =="5":
    choice = "Spock"
else:
    print("!!!INVALID CHOICE!!! \nENDING PROGRAM!")
    exit() # Ending program if invalid choice
possible_actn = ["Rock","Paper","Scissors","Lizard","Spock"] # All the possible output for
computer_actn = random.choice(possible_actn) # Randomising the computer values

#Printing choices
print(f"\nYour choice is {choice}, and computer's choice is {computer_actn}. \n")

#IT's A TIE!
if choice == computer_actn:
    print("It's a tie!")

#Rock choices
elif choice == "Rock":
    if computer_actn == "Paper":
        print("The computer won!")
    elif computer_actn == "Scissors":
        print("You won!")
    elif computer_actn == "Lizard":
        print("You won!")
    elif computer_actn == "Spock":
        print("The computer won!")

#Paper choices
elif choice == "Paper":
    if computer_actn == "Rock":
        print("You won!")
    elif computer_actn == "Scissors":
        print("The computer won!")
    elif computer_actn == "Lizard":
        print("The computer won!")
    elif computer_actn == "Spock":
        print("You won!")

#Scissors choices
elif choice == "Scissors":
    if computer_actn == "Paper":
        print("You won!")
    elif computer_actn == "Rock":
        print("The computer won!")
    elif computer_actn == "Lizard":
        print("You won!")
    elif computer_actn == "Spock":
        print("The computer won!")

#Lizard choices
elif choice == "Lizard":
    if computer_actn == "Paper":
        print("You won!")
    elif computer_actn == "Scissors":
        print("The computer won!")
    elif computer_actn == "Rock":
        print("The computer won!")
    elif computer_actn == "Spock":
        print("You won!")

#Spock choices
elif choice == "Spock":
    if computer_actn == "Paper":
        print("The computer won!")
    elif computer_actn == "Scissors":
        print("You won!")
    elif computer_actn == "Lizard":
        print("The computer won!")
    elif computer_actn == "Rock":
        print("You won!")