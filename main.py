from art import logo
from menu import MENU, resources, profit

money = 0


def process_coins():
    print('Please inert coins.')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def check_resources(quantity_ingredient):
    for item in quantity_ingredient:
        if quantity_ingredient[item] > resources[item]:
            print(f'Sorry, there is not enough {item}.')
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry, thet\'s not enough money. Money refunded.')
        return False


def make_order(choice, resources):
    for item in choice['ingredients']:
        resources[item] -= choice['ingredients'][item]
    print(f"Here is your {orders} ☕️. Enjoy!")


is_on = True

while is_on:
    print(logo)
    orders = input('What would you like? (espresso, latte, cappuccino): ')
    if orders == 'off':
        is_on = False
    elif orders == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: #{resources["profit"]}')
    else:
        choice = MENU[orders]
        if check_resources(choice['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, choice['cost']):
                make_order(choice, choice['ingredients'])
