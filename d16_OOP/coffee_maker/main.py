from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_continue = True

while is_continue:
    choice = input(f"What would you like? ({Menu.get_items()}):")
    if choice == "report":
        coffee_maker.report()
    elif choice == "off":
        is_continue = False
    else:
        drink = Menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

