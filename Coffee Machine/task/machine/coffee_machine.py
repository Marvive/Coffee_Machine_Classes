
class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def start_machine(self):
        options = ""
        while options != "exit":
            options = input("Write action (buy, fill, take, remaining:)")
            if options == "buy":
                types = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                if types == "1":
                    self.water -= 250
                    self.coffee_beans -= 16
                    self.money += 4
                    self.disposable_cups -= 1
                    for each in [self.water, self.milk, self.coffee_beans, self.disposable_cups]:
                        if each < 0:
                            if self.water < 0:
                                message = "water"
                            elif self.coffee_beans < 0:
                                message = "coffee beans"
                            elif self.disposable_cups < 0:
                                message = "disposable_cups"
                            else:
                                message = "Error"
                            self.water += 250
                            self.coffee_beans += 16
                            self.money -= 4
                            self.disposable_cups += 1
                            print(f"Sorry, not enough {message}!")
                            break

                elif types == "2":
                    self.water -= 350
                    self.milk -= 75
                    self.coffee_beans -= 20
                    self.money += 7
                    self.disposable_cups -= 1
                    for each in [self.water, self.milk, self.coffee_beans, self.disposable_cups]:
                        if each < 0:
                            if self.water < 0:
                                message = "water"
                            elif self.coffee_beans < 0:
                                message = "coffee beans"
                            elif self.disposable_cups < 0:
                                message = "disposable_cups"
                            elif self.milk < 0:
                                message = "milk"
                            else:
                                message = "Error"
                            self.water += 350
                            self.coffee_beans += 20
                            self.money -= 7
                            self.milk += 75
                            self.disposable_cups += 1
                            print(f"Sorry, not enough {message}!")
                            break
                elif types == "3":
                    self.water -= 200
                    self.milk -= 100
                    self.coffee_beans -= 12
                    self.money += 6
                    self.disposable_cups -= 1
                    # if min(amounts.values()) < 0:
                    for each in [self.water, self.milk, self.coffee_beans, self.disposable_cups]:
                        if each < 0:
                            if self.water < 0:
                                message = "water"
                            elif self.coffee_beans < 0:
                                message = "coffee beans"
                            elif self.disposable_cups < 0:
                                message = "disposable_cups"
                            elif self.milk < 0:
                                message = "milk"
                            else:
                                message = "Error"
                            self.water += 200
                            self.coffee_beans += 12
                            self.money -= 6
                            self.milk += 100
                            self.disposable_cups += 1
                            print(f"Sorry, not enough {message}!")
                            break
                elif types == "back":
                    continue

            elif options == "fill":
                water_add = int(input("Write how many ml of water do you want to add:"))
                milk_add = int(input("Write how many ml of milk do you want to add:"))
                coffee_add = int(input("Write how many grams of coffee beans do you want to add:"))
                disposable_cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
                self.water += water_add
                self.milk += milk_add
                self.coffee_beans += coffee_add
                self.disposable_cups += disposable_cups_add
            elif options == "take":
                print(f"I gave you ${self.money}")
                self.money = 0
            elif options == "remaining":
                print(f"""The coffee machine has:
                {self.water} of water
                {self.milk} of milk
                {self.coffee_beans} of coffee beans
                {self.disposable_cups} of disposable cups
                {self.money} of money""")


current_machine = CoffeeMachine(400, 540, 120, 9, 550)
current_machine.start_machine()
