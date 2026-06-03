while True: 
    weight =(input("enter your weight please: (q to Quit) "))
    if weight == "q":
        break

    weight = float(weight)
    unit = input("Kilograms or Pound? (kg or lbs) :")

    if unit.lower()== "kg":
        weight = weight * 2.205
        unit = "lbs"
        print(f"Your weight is: {round(weight,2)} {unit}")
    elif unit.lower() == "lbs":
        weight = weight / 2.205
        unit = "kgs"  
        print(f"your weight is: {round(weight,2)} {unit}")
    else :
        print(f"Your {unit} is not valid")

