# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# TODO-2: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(start_text, amount_shift, direction_cipher):
    end_text = ''
    if direction_cipher == 'decode':
        amount_shift *= -1  # n * 1 = n or n * (-1) = -n Depends on whether we have to subtract or add!
    for letter in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + amount_shift
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f'Here\'s the {direction}d result: {end_text}')


# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # TODO-5: What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift % 26

    # TODO-6: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
    caesar(start_text=text, amount_shift=shift, direction_cipher=direction)

    restart = input('Type "yes" if you want to go again. Otherwise type "no".\n')
    if restart == 'no':
        should_end = True
        print('Goodbye')
        break
