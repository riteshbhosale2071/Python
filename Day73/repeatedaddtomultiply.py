def convert():
    number = int(input("Enter the repeated number: "))
    times = int(input("How many times is it added? "))

    print(f"{number} + " * (times - 1) + str(number))
    print(f"Multiplication Form = {number} × {times}")

convert()