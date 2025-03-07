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
    "coffee": 100,
}
should_stop=False
money=0
def check_resources(ingredients,resources):   
    water=ingredients['water']
    coffee=ingredients['coffee']
    try:
        milk=ingredients['milk']
        
        print(resources['water'])
        if water>resources['water'] and coffee>resources['water'] and milk>resources['milk']:
            print("Sorry there are not enough resources")
            return False
    except KeyError as ke:
        if water>resources['water'] and coffee>resources['water']:
            print("Sorry there are not enough resources")
            return False
    return True
def process_coins():
    print("insert coins")
    total=float(input("enter number of quarters: "))*0.25
    total+=float(input("enter number of dimes: "))*0.10
    total+=float(input("enter number of nickles: "))*0.05
    total+=float(input("enter number of pennis: "))*0.01
    return total
def transaction_success(cost,total):
    global money
    if total<cost:
        print("sorry that's not enough money")
    else:
        money+=total-cost
while should_stop!=True:
    user_input=input("What would you like? (espresso/latte/cappuccino):​")
    if user_input=='off':
        should_stop=True
        break
    elif user_input=='report':
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"money={money}")
    else:
        if check_resources(MENU[user_input]['ingredients'],resources):
            total=process_coins()
            print(f"monetary value inserted{total}")
            transaction_success(MENU[user_input]['cost'],total)
        else:
            print("invalid value error")
