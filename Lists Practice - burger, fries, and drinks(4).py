burgers = []
fries = []
drinks = []

count = 1

while count < 100:
    burger_amount = int(input("How many burgers would you like to purchase: "))
    burgers.append(burger_amount)

    fries_amount = int(input("How many fries would you like to purchase: "))
    fries.append(fries_amount)

    drink_amount = int(input("How many drinks would you like to purchase: "))
    drinks.append(drink_amount)

    count += 1

total_burger = sum(burgers)
total_fries = sum(fries)
total_drink = sum(drinks)

print(f"Burgers: {total_burger}\nFries: {total_fries}\nDrinks: {total_drink}")
