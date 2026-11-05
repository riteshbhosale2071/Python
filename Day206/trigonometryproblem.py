import random
import math

def trigonometryproblem():
    print("Trigonometry Problem Generator")
    print("1. Find a trigonometric ratio")
    print("2. Find a missing side")
    print("3. Find a missing angle")

    choice = input("Enter your choice (1-3): ")

    angles = [30, 45, 60]

    if choice == "1":
        angle = random.choice(angles)
        ratio = random.choice(["sin", "cos", "tan"])

        if ratio == "sin":
            answer = math.sin(math.radians(angle))
        elif ratio == "cos":
            answer = math.cos(math.radians(angle))
        else:
            answer = math.tan(math.radians(angle))

        print(f"\nProblem: Find {ratio}({angle}°).")
        input("Press Enter to reveal the answer...")
        print("Answer:", round(answer, 4))

    elif choice == "2":
        angle = random.choice(angles)
        adjacent = random.randint(3, 15)
        opposite = adjacent * math.tan(math.radians(angle))

        print(f"\nProblem: A right triangle has an angle of {angle}°")
        print(f"and an adjacent side of {adjacent} units.")
        print("Find the opposite side.")

        input("Press Enter to reveal the answer...")
        print("Answer:", round(opposite, 2), "units")

    elif choice == "3":
        opposite = random.randint(3, 15)
        adjacent = random.randint(3, 15)
        angle = math.degrees(math.atan(opposite / adjacent))

        print(f"\nProblem: A right triangle has opposite side {opposite}")
        print(f"and adjacent side {adjacent} units.")
        print("Find the angle.")

        input("Press Enter to reveal the answer...")
        print("Answer:", round(angle, 2), "degrees")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

trigonometryproblem()