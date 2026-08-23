def cubenumber():
    terms = int(input("Enter the number of terms: "))

    if terms <= 0:
        print("Enter a positive number of terms.")
        return

    print("Cube Number Pattern:")

    for i in range(1, terms + 1):
        print(i ** 3, end=" ")

cubenumber()