# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')t
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from pretty_tables import PrettyTables


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    items = menu.get_items()
    choice = input(f"What would you like {items}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)

headers = ['ID', 'Name', 'Occupation', 'Employed']
rows = [
    [1, 'Justin', 'Software Engineer', True],
    [2, 'Misty', 'Receptionist', False],
    [3, 'John', None, False],
]

table = PrettyTables.generate_table(headers=headers, rows=rows, empty_cell_placeholder='No data')

print(table.center(10))

print(table)

