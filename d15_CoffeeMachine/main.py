MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 50,
}
profit = 0

is_continue = True


def check_ingredient(coffee):
    for key in MENU[coffee]["ingredients"]:
        if resources[key] < MENU[coffee]["ingredients"][key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def check_transaction(coffee, money):
    if money > MENU[coffee]["cost"]:
        change = round(money - MENU[coffee]["cost"], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee} ☕️. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while is_continue:
    type = input("What would you like? (espresso/latte/cappuccino):").lower()
    if type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if check_ingredient(type):
            print("Please insert coins.")

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            print(f"Total: {total}")

            if check_transaction(type, total):
                for key in MENU[type]['ingredients']:
                    resources[key] -= MENU[type]['ingredients'][key]
                profit += MENU[type]['cost']
