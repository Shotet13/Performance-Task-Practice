import random

random_num = random.randint(1,100)

while True:
    num = int(input())
    if random_num > num:
        print("too low")
    elif random_num < num:
        print("too high")
    else:
        print("equal")
        break
