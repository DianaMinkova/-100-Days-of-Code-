from art import logo
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


# Make function to set difficulty.
def choose_level():
    set_level = input('Choose a difficulty. Type "easy" or "hard": ').lower()
    if set_level == 'easy':
        return EASY_ATTEMPTS
    elif set_level == 'hard':
        return HARD_ATTEMPTS


# Function to check user's guess against actual answer.
def check_number(guess_number, turns, think_of_a_number):
    """Check answer against guess. Returns the number of turns remaining."""
    if guess_number > think_of_a_number:
        print('Too high.')
        return turns - 1
    elif guess_number < think_of_a_number:
        print('Too low.')
        return turns - 1
    else:
        print(f'You dot it! The number was {think_of_a_number}')


def game():
    print(logo)

    # Choosing a random number between 1 and 100.
    print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')
    answer = randint(1, 100)
    print(f'Pass, the correct answer is {answer}')

    turns_num = choose_level()

    # Repeat the guessing function if they get it wrong.
    guess = 0
    while guess != answer:
        print(f'You have {turns_num} attempts remaining to guess the number.')

        # let the user guess a number.
        guess = int(input('Make a guess: '))

        turns_num = check_number(guess, turns_num, answer)
        if turns_num == 0:
            print('You\'ve run out of guesses, you lose')
            return
        elif guess != answer:
            print('Guess again')


game()
