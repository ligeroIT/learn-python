weight = int(input("Please prowide your package weight: "))
ground_flat_charge = 20.00
premium_flat_charge = 120.00
cost = 0


while True:
    d1a = input(
        "Do you want ship your package by: A) Ground Shipping. B) Ground Shipping Premium. C) Drone Shipping [A/B/C]?: ")
    if d1a == "A":
        if weight <= 2:
                cost = weight * 1.50 + ground_flat_charge
        elif 2 < weight <= 6:
                cost = weight * 3.00 + ground_flat_charge
        elif 6 < weight <= 10:
                cost = weight * 4.00 + ground_flat_charge
        else:
                cost = weight * 4.75 + ground_flat_charge
        print("You choose Ground Shipping. Cost: $", cost)
        break
    elif d1a == "B":
        cost = premium_flat_charge
        print("You choose Ground Shipping Premium. Cost: $", cost)
        break
    elif d1a == "C":
        if weight <= 2:
            cost = weight * 4.50
        elif 2 < weight <= 6:
            cost = weight * 9.00
        elif 6 < weight <= 10:
            cost = weight * 12.00
        else:
            cost = weight * 14.00
        print("You choose Drone Shipping. Cost: $", cost)
        break
    else:
        print("Please pickup again")
