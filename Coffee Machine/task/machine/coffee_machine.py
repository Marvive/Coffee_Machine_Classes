# Write your code here
# print("""Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!""")

# cups = int(input())
# print(f"""For {cups} cups of coffee you will need
# {cups * 200} ml of water
# {cups * 50} ml of milk
# {cups * 15} g of coffee beans""")

# water = int(input("Write how many ml of water the coffee machine has:"))
# milk = int(input("Write how many ml of water the coffee machine has:"))
# coffee = int(input("Write how many ml of water the coffee machine has:"))
# cups = int(input("Write how many ml of water the coffee machine has:"))
# max_coffee = min([(water // 200), (milk // 50), (coffee // 15)])
# if cups <= max_coffee:
#     print(f"Yes, I can make that amount of coffee (and even {max_coffee - cups} more than that)")
# else:
#     print(f"No, I can make only {max_coffee} cups of coffee")

amounts = {
    "water": 400,
    "milk": 540,
    "coffee_beans": 120,
    "disposable_cups": 9,
    "money": 550,
}
# water = 400
# milk = 540
# coffee_beans = 120
# disposable_cups = 9
# money = 550


def supplies():
    print(f"""The coffee machine has:
    {amounts["water"]} of water
    {amounts["milk"]} of milk
    {amounts["coffee_beans"]} of coffee beans
    {amounts["disposable_cups"]} of disposable cups
    {amounts["money"]} of money""")


options = ""
while options != "exit":
    options = input("Write action (buy, fill, take, remaining:)")
    if options == "buy":
        types = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if types == "1":
            amounts["water"] -= 250
            amounts["coffee_beans"] -= 16
            amounts["money"] += 4
            amounts["disposable_cups"] -= 1
            if min(amounts.values()) < 0:
                if amounts["water"] < 0:
                    message = "water"
                elif amounts["coffee_beans"] < 0:
                    message = "coffee beans"
                elif amounts["disposable_cups"] < 0:
                    message = "disposable_cups"
                else:
                    message = "Error"
                amounts["water"] += 250
                amounts["coffee_beans"] += 16
                amounts["money"] -= 4
                amounts["disposable_cups"] += 1
                print(f"Sorry, not enough {message}!")

        elif types == "2":
            amounts["water"] -= 350
            amounts["milk"] -= 75
            amounts["coffee_beans"] -= 20
            amounts["money"] += 7
            amounts["disposable_cups"] -= 1
            if min(amounts.values()) < 0:
                if amounts["water"] < 0:
                    message = "water"
                elif amounts["coffee_beans"] < 0:
                    message = "coffee beans"
                elif amounts["disposable_cups"] < 0:
                    message = "disposable_cups"
                elif amounts["milk"] < 0:
                    message = "milk"
                else:
                    message = "Error"
                amounts["water"] += 350
                amounts["coffee_beans"] += 20
                amounts["money"] -= 7
                amounts["milk"] += 75
                amounts["disposable_cups"] += 1
                print(f"Sorry, not enough {message}!")
        elif types == "3":
            amounts["water"] -= 200
            amounts["milk"] -= 100
            amounts["coffee_beans"] -= 12
            amounts["money"] += 6
            amounts["disposable_cups"] -= 1
            if min(amounts.values()) < 0:
                if amounts["water"] < 0:
                    message = "water"
                elif amounts["coffee_beans"] < 0:
                    message = "coffee beans"
                elif amounts["disposable_cups"] < 0:
                    message = "disposable_cups"
                elif amounts["milk"] < 0:
                    message = "milk"
                else:
                    message = "Error"
                amounts["water"] += 200
                amounts["coffee_beans"] += 12
                amounts["money"] -= 6
                amounts["milk"] += 100
                amounts["disposable_cups"] += 1
                print(f"Sorry, not enough {message}!")
        elif types == "back":
            continue

    elif options == "fill":
        water_add = int(input("Write how many ml of water do you want to add:"))
        milk_add = int(input("Write how many ml of milk do you want to add:"))
        coffee_add = int(input("Write how many grams of coffee beans do you want to add:"))
        disposable_cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        amounts["water"] += water_add
        amounts["milk"] += milk_add
        amounts["coffee_beans"] += coffee_add
        amounts["disposable_cups"] += disposable_cups_add
    elif options == "take":
        print(f"I gave you ${amounts['money']}")
        amounts["money"] = 0
    elif options == "remaining":
        supplies()









