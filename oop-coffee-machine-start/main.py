from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = Menu()
items = menu_item.get_items()
maker = CoffeeMaker()
finance = MoneyMachine()
operational = True
while operational:
    request = input(f"What would you like? ({items }): ")
    if request == 'report':
        maker.report()
        finance.report()
    elif request == 'off':
        operational = False
    else:
        order = menu_item.find_drink(request)
        if maker.is_resource_sufficient(order):
            if finance.make_payment(order.cost):
                maker.make_coffee(order)




