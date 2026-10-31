import random
import math

def triangleconstructionpractice():
    print("Triangle Construction Practice Generator")
    print("1. SSS")
    print("2. SAS")
    print("3. ASA")
    print("4. Mixed Practice")

    choice = input("Choose a practice type (1-4): ")

    if choice == "1":
        a = random.randint(3, 10)
        b = random.randint(3, 10)
        c = random.randint(abs(a - b) + 1, a + b - 1)

        while a + b <= c or a + c <= b or b + c <= a:
            a = random.randint(3, 10)
            b = random.randint(3, 10)
            c = random.randint(3, 10)

        print(f"\nConstruct a triangle with sides {a}, {b}, and {c}.")
        print("Condition: SSS")

    elif choice == "2":
        a = random.randint(4, 12)
        b = random.randint(4, 12)
        angle = random.choice([30, 45, 60, 90, 120])

        third_side = math.sqrt(
            a**2 + b**2 - 2 * a * b * math.cos(math.radians(angle))
        )

        print(f"\nConstruct a triangle with sides {a} and {b}.")
        print(f"The included angle is {angle} degrees.")
        print(f"Find the third side. (Approximate value: {third_side:.2f})")
        print("Condition: SAS")

    elif choice == "3":
        angle_a = random.choice([30, 45, 60, 75])
        angle_b = random.choice([30, 45, 60, 75])

        while angle_a + angle_b >= 180:
            angle_a = random.choice([30, 45, 60, 75])
            angle_b = random.choice([30, 45, 60, 75])

        side = random.randint(5, 15)

        print(f"\nConstruct a triangle with angles {angle_a} and {angle_b}.")
        print(f"The included side is {side} units.")
        print("Condition: ASA")

    elif choice == "4":
        practice_type = random.choice(["SSS", "SAS", "ASA"])

        if practice_type == "SSS":
            a, b, c = 5, 6, 7
            print(f"\nConstruct a triangle with sides {a}, {b}, and {c}.")
        elif practice_type == "SAS":
            print("\nConstruct a triangle with sides 6 and 8.")
            print("The included angle is 60 degrees.")
        else:
            print("\nConstruct a triangle with angles 45 and 60 degrees.")
            print("The included side is 8 units.")

        print("Condition:", practice_type)

    else:
        print("Invalid choice. Select a number from 1 to 4.")

triangleconstructionpractice()