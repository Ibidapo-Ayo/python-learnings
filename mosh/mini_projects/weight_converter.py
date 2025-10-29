import math
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ").lower()

if unit in ["lbs", "lb", "kg", "kgs", "l", "k"]:
        print(f"You are {math.floor(weight * 0.45)} kilograms")
elif unit in ["kg", "kgs", "k"]:
        print(f"You are {math.floor(weight / 0.45)} pounds")
else:
        print("Invalid unit")