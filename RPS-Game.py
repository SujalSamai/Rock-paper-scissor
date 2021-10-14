
import random

print("\nHello!! Welcome to Rock-Paper-Scissor Game\n")
print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->Paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->Scissor wins \n")

while True:
    print("Enter your choice: \n 1. Rock \n 2. Paper \n 3. Scissor \n")

    choice = int(input("Your turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("Please Enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'

    print("Okay, so your choice is: " + choice_name)
    print("\nNow its computer turn.......")

    computer = random.randint(1, 3)

    while computer == choice:
        computer = random.randint(1, 3)

    if computer == 1:
        comp_choice_name = 'Rock'
    elif computer == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'

    print("\nComputer choice is: " + comp_choice_name)

    print("So it's " + choice_name + " V/s " + comp_choice_name)
    print("Hmm, let's see what's the result..")
    print("\nSo the result is...")

    # condition for winning
    if((choice == 1 and computer == 2) or
            (choice == 2 and computer == 1)):
        print("Paper wins as Paper will crush Rock\n")
        result = "paper"

    elif((choice == 1 and computer == 3) or
            (choice == 3 and computer == 1)):
        print("Rock wins as Rock will break Scissors\n")
        result = "Rock"
    else:
        print("scissor wins as Scissor will cut Paper\n")
        result = "scissor"

    # Printing either user or computer wins
    if result == choice_name:
        print("Congratulations!!! You won.. Hurraaah!!")
    else:
        print("Sorry! Computer Won, better luck next time..")

    print("\nDo you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print("\nThanks for playing")
