menu = {"Pizza" : 300,
        "Momo": 120,
        "Noodles" : 120,
        "Pasta" : 180,
        "Spring Roll" : 150,
        "chilli Potato" : 200,
        "Soda" : 60,
        "Fries" : 150}

cart = []
total = 0

print("--------------MENU-------------")
for key , value in menu.items() :
    print(f"{key:10} : ${value:.2f}")
print("--------------------------------")  

while True:
    food = input("Select the item (q to quit): ").title()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------------YOUR ORDER-----------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()    
print(f"Your total is : ${total:.2f} ")