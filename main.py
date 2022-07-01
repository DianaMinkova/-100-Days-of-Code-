# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
# All method # https://www.w3schools.com/python/python_ref_file.asp
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = '[name]'  # it is necessary to replace the name with the name of people from invited_names.txt

with open('./input/Names/invited_names.txt', 'r') as names_file:
    names = names_file.readlines()
    # print(names) => ['Diana\n', 'Ivan\n', 'Nikol\n', 'Emi\n', 'Alex']

with open('./input/Letters/starting_letter.txt', 'r') as letter_file:
    letter_content = letter_file.read()
    # print(letter_content) => all text from starting_letter.txt

    for name in names:
        strip_name = name.strip()  # Removes superfluous characters (in case \n)
        new_letter = letter_content.replace('[name]', strip_name)  # Replace the word in text

        with open(f'./Output/ReadyToSend/letter_for_{strip_name}.txt', 'w') as mail_file:
            mail_file.write(new_letter) # save new letter in new fail
