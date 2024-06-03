while True:
    gender = str(input("Input male, female, other (type enter to stop code): "))
    if gender == "male":
        print("Good morning Sir")
    elif gender == "female":
        print("Good morning Maam")
    elif gender == "other":
        print("Good morning Person")
    else:
        break
