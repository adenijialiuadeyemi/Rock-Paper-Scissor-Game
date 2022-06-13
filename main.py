# we import random to randomize the computer’s actions in the game
import random

# Print multiline instruction
# perform string concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")


#Running a loop for the game to be played severally
while True:
    
    #Taking input from a user
    user_action = input("Enter a choice ('R' for rock, 'P' for paper, 'S' for scissors): ").upper()

    #looping until user enter invalid input
    if user_action != 'R' or user_action != 'P' or user_action != 'S':
       print ("Wrong Input. Please, Enter a valid input\n")
       user_action = input("Enter a choice ('R' for rock, 'P' for paper, 'S' for scissors): ").upper()       
   
 
    # initialize value of choice_name variable
    # corresponding to the choice value
    if user_action == 'R':
        choice_name1 = 'Rock'
    elif user_action == 'P':
        choice_name1 = 'paper'
    else:
        choice_name1 = 'scissor'
         
    # print user choice
    print("user choice is: " + choice_name1)
    print("\nNow its computer turn.......")
 

    #making the computer choose a random value
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)

    if computer_action == 'R':
        choice_name2 = 'Rock'
    elif computer_action == 'P':
        choice_name2 = 'paper'
    else:
        choice_name2 = 'scissor'

    print("Computer choice is: " + choice_name2)
    

    #printing the choices of the user and the computer
    print(f"\nTherefore we have: ----> Player ({choice_name1}) : Computer ({choice_name2}).\n")

    #We determine the winner as follows
    if user_action == computer_action:
        print(f"Both players selected {choice_name1}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose, Computer Wins.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose,  Computer Wins.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose,  Computer Wins.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")
