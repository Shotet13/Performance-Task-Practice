while True:
    burgers = float(input("Number of burgers ordered: "))
    fries = float(input("Number of fries ordered: "))
    drinks = float(input("Number of drinks ordered: "))
    b = burgers * 3.49
    f = fries * 1.99
    d = drinks * 1.29
    final = (b + f + d) + ((b + f + d) * 0.13)
    if burgers == 0 and fries == 0 and drinks == 0:
        print("\nSorry we're closed")
        break
    else:
        print(f"\nBill:\nBurger Cost: {b}\nFries Cost: {f}\nDrinks Cost: {d}\n\nFinal Cost: {final}\n")
