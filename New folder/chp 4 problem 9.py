my_pizzas = ["pepperoni", "margherita", "bbq chicken"]
friend_pizzas = my_pizzas.copy()
my_pizzas.append("hawaiian")
friend_pizzas.append("veggie")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
