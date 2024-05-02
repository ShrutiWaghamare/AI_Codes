import random

def number_guessing_game():
    number = random.randint(1, 100)
    guesses = 0

    while guesses < 10:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number:
            print("Congratulations! You guessed the number correctly!")
            break
        elif guess < number:
            print("Your guess was too low.")
        else:
            print("Your guess was too high.")
        guesses += 1

    if guesses == 10:
        print("Sorry, you ran out of guesses. The number was", number)

def rock_paper_scissors():
    print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
          'Rock vs Paper -> Paper wins \n'
          'Rock vs Scissors -> Rock wins \n'
          'Paper vs Scissors -> Scissor wins \n')

    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
        choice = int(input("Enter your choice: "))
        while choice not in [1, 2, 3]:
            choice = int(input('Enter a valid choice please: '))

        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'

        print('User choice is:', choice_name)
        comp_choice_name = random.choice(['Rock', 'Paper', 'Scissors'])
        print("Computer choice is:", comp_choice_name)
        print(choice_name, 'Vs', comp_choice_name)

        if choice_name == comp_choice_name:
            print('It\'s a Draw')
        elif (choice == 1 and comp_choice_name == 'Paper') or \
             (choice == 2 and comp_choice_name == 'Scissors') or \
             (choice == 3 and comp_choice_name == 'Rock'):
            print('Computer wins')
        else:
            print('User wins')

        play_again = input("Do you want to play again? (Y/N)").lower()
        if play_again != 'y':
            break

def chatbot():
    print("Hello! Welcome to the game hub.")
    while True:
        print("Select the game you want to play:")
        print("1. Guess the Number")
        print("2. Rock Paper Scissors")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            number_guessing_game()
        elif choice == 2:
            rock_paper_scissors()
        elif choice == 3:
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select again.")

chatbot()
