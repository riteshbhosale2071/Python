import random

def quadraticequation():
    print("Quadratic Equation :")

    count = int(input("How many quadratic equations do you want to generate? "))

    if count <= 0:
        print("Enter a positive number of equations.")
        return

    print("\nGenerated Quadratic Equations:")

    for i in range(1, count + 1):
        a = random.choice([x for x in range(-10, 11) if x != 0])
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)

        print(f"{i}. {a}x² + {b}x + {c} = 0")

quadraticequation()