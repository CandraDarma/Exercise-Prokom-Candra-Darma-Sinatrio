pizzas = ["pepperoni", "margherita", "hawaiian"]
friend_pizzas = pizzas[:]

pizzas.append("meat lovers")
friend_pizzas.append("veggie")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
