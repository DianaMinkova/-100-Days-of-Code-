from random import choice
from hangman_art import stages, logo
from hangman_word import word_list
from replit import clear


chosen_word = choice(word_list)
end_the_game = False
lives = 6


print(logo)

#Testing code:
#print(f'Pssst, the solution is {chosen_word}.')


lend_word = len(chosen_word)
display = []
'''First solution'''
# for letter in chosen_word:
#     display.append('_')
'''Second solution'''
# for _ in range(lend_word):
#     display += '_'
# '''list comprehension solution'''
[display.append('_') for letter in chosen_word]

#Testing code:
#print(' '.join(display))

while not end_the_game:
    guess = input('Guess a letter: ').lower()

    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f'You\'ve already guessed {guess}')

    for index in range(lend_word):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = guess

    print(f'{" ".join(display)}')
    # print('You win')

    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')

        lives -= 1
        if lives == 0:
            end_the_game = True
            print('You lost.')
    print(stages[lives])

    if '_' not in display:
        end_the_game = True
        print('You win')
