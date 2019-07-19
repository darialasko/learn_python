age = input("How old are you?")

if age:
    age = int(age)
    if age >= 21:
        print("Normal entry")
    elif 18 < age:
        print("Wristband")
    else:
        print("too young, sorry")
else:
    print("It isn't a number")