import random

nums = []

def rng(max_num):
    return random.randint(1, max_num)

MAX = int(input("Enter an integer for MAX: "))

for _ in range(50):
    random_number = rng(MAX)
    nums.append(random_number)

for num in nums:
    print(num)
