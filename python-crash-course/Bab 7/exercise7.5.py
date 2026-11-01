while True:
    age = input("How old are you? (type 'quit' to stop) ")
    if age == "quit":
        break

    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")