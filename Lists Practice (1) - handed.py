left = []
right = []
ambidextrous = []

while True:
    print("Input stop to exit the code at anytime")
    
    name = input(str("Please input your name: "))
    if name == "stop":
        break
        
    hand = input(str("Please input if you're left-handed, right-handed, or ambidextrous: "))
    if hand == "stop":
        break
        
    if hand == 'left-handed':
        left.append(name)
    elif hand == "right-handed":
        right.append(name)
    else:
        ambidextrous.append(name)


print("\nLeft-handed People: ")
for name in left:
    print(name)

print("\nRight-handed People: ")
for name in right:
    print(name)

print("\nAmbidextous People: ")
for name in ambidextrous:
    print(name)
