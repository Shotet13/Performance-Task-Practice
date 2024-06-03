pets = ['gilbert']

while True:
    choice = input("\n1. Add \n2. Remove \n3. Search \n4. List \n5. Exit \n\nChoice: ")
    
    if choice == '1':
        add = input("\nWhat pet would you like to add?\n")
        pets.append(add)
    elif choice == '2':
        remove = input("\nWhat pet would you like to remove?\n")
        pets.remove(remove)
    elif choice == '3':
        search = input("\nWhat pet would you like to search for?\n")
        if search in pets:
            print("\nIn stock\n")
        else:
            print("\nNot in stock\n")
    elif choice == '4':
        print(pets)
    elif choice == '5':
        break
    else:
        print("\nInvalid\n")
