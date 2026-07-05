import random

def missingdigit():
    num1 = random.randint(10, 99)
    num2 = random.randint(2, 9)

    product = num1 * num2

    product_str = str(product)

    position = random.randint(0, len(product_str) - 1)
    missing_digit = product_str[position]

    puzzle = ""

    for i in range(len(product_str)):
        if i == position:
            puzzle += "_"
        else:
            puzzle += product_str[i]

    print("\nMissing Digit Multiplication Puzzle")
    print("-" * 40)
    print(f"{num1} × {num2} = {puzzle}")

    answer = input("Enter the missing digit: ")

    if answer == missing_digit:
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Digit =", missing_digit)

missingdigit()