def distribution():
    total_water = float(input("Enter total water (liters): "))
    
    people = int(input("Enter number of people: "))

    water_per_person = total_water / people

    print("Water per Person =", round(water_per_person, 2), "liters")

distribution()