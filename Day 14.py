from art import logo, vs
from random import sample
from game_data import data


def get_random_account():
    return sample(data, 2)


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'


def check_answer(follower_guess, follower_a, follower_b):
    if follower_a['follower_count'] > follower_b['follower_count']:
        return follower_guess == 'a'
    else:
        return follower_guess == 'b'


def game():
    print(logo)
    game_should_continue = True
    score = 0

    while True:
        account_a, account_b = get_random_account()

        print(format_data(account_a))
        print(vs)
        print(format_data(account_b))
        guess = input(f'Who has more followers? Type "A" or "B": ').lower()

        correct_answer = check_answer(guess, account_a, account_b)

        if correct_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
            return


game()
