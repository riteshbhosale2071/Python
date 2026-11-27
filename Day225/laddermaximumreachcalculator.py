import math

def laddermaximumreachcalculator():
    print("Ladder Maximum Reach Calculator")
    print("1. Calculate maximum vertical reach")
    print("2. Calculate minimum ladder length")
    print("3. Calculate horizontal distance from wall")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        length = float(input("Enter ladder length: "))
        angle = float(input("Enter angle between ladder and ground: "))

        if length <= 0 or not 0 < angle <= 90:
            print("Invalid measurements.")
            return

        reach = length * math.sin(math.radians(angle))
        print("Maximum Vertical Reach =", round(reach, 2), "units")

    elif choice == "2":
        height = float(input("Enter required vertical height: "))
        angle = float(input("Enter angle between ladder and ground: "))

        if height <= 0 or not 0 < angle <= 90:
            print("Invalid measurements.")
            return

        length = height / math.sin(math.radians(angle))
        print("Minimum Ladder Length =", round(length, 2), "units")

    elif choice == "3":
        length = float(input("Enter ladder length: "))
        angle = float(input("Enter angle between ladder and ground: "))

        if length <= 0 or not 0 < angle <= 90:
            print("Invalid measurements.")
            return

        distance = length * math.cos(math.radians(angle))
        print("Horizontal Distance from Wall =", round(distance, 2), "units")

    else:
        print("Invalid choice.")

laddermaximumreachcalculator()