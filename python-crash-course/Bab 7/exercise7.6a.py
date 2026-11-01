topping = ""
while topping != "quit":
    topping = input("Enter a topping (type 'quit' to stop): ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")