from random import randint

# Computer Moves 
computer_moves  = ["Rock","Paper", "Scissors"]

#Making computer moves random 
computer = computer_moves[randint(0,2)]

#Controls game going
while True:
    # Keep asking for player input
    player_move = input("Rock? Paper? Scissors? ")

    #Checking to see if player input is vaild
    if player_move.capitalize() in computer_moves:
    
    #Check to see if player won
        if player_move.capitalize() == computer:
            print("Tie!")
            print(f"Player was {player_move.capitalize()} and Computer was {computer}!")
        
            break
        elif player_move.capitalize() == 'Rock' and computer == 'Scissors':
            print("Player Wins!")
            print(f"Player was {player_move.capitalize()} and Computer was {computer}!")
            break
        elif player_move.capitalize() == 'Paper' and computer == 'Rock':
            print("Player Wins!")
            print(f"Player was {player_move.capitalize()} and Computer was {computer}!")
            break
        elif player_move.capitalize() == 'Scissors' and computer == 'Paper':
            print("Player Wins!")
            print(f"Player was {player_move.capitalize()} and Computer was {computer}!")
            break
        else: 
            print("Computer Wins!")
            print(f"Computer was {computer} and Player was {player_move.capitalize()}!")
            break
    else:
        print("Invalid Move!Try again")

        