#for x in range(1,21):
#    if x == 4 or x == 13:
#        print(f"Lucky number {x} ")
#    elif x % 2 == 0:
#        print(f"Number {x} is even")
#    else:
#        print(f"Number {x} is odd")

for x in range(1,21):
    if x == 4 or x == 13:
        text = "lucky"
    elif x % 2 == 0:
        text = "even"
    else:
        text = "odd"
    print(f"Number {x} is {text}")