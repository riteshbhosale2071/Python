def wheel():
    number = int(input("Enter a number: "))

    print("\nMultiplication Wheel")

    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")

wheel()