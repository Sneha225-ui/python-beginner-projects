#Shopping Cart Program
foods = []
prices = []
total = 0

while True :
    food = input("enter the food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else :
        price = float(input(f"enter the price {food}: $ "))

        foods.append(food)
        prices.append(price)

print("--------YOUR CART--------")
for food in (foods):
    print(food, end=" ")
for price in prices:
    total += price

print()
print(f"Your total bill is: {total}")


