from pandas import DataFrame, read_csv

date = read_csv('nato_phonetic_alphabet.csv')  # Reade data file letter,code 1row => A,Alfa, 2row => B,Bravo
#print(date)  # letter code 0 A Alfa, 1 B Bravo

data_dict = {row.letter: row.code for (index, row) in date.iterrows()}  # Convert date to dictionary
#print(data_dict)  # {'A': 'Alfa', 'B': 'Bravo',.....}

run_again = True
while run_again:
    word = input('Enter a word: ').upper()
    # nested for loop with List Comprehension:
    # result = [code for let in word for letter, code in data_dict.items() if let == letter]
    # print(result)  # ['Whiskey', 'Oscar', 'Romeo', 'Delta']

    output_list = [data_dict[letter] for letter in word ]   # Reading element of a dict/list using same element (data_dict[letter])
    print(output_list)  # ['Whiskey', 'Oscar', 'Romeo', 'Delta']

