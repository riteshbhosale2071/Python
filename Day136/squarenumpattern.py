def squarenumberpattern():
    terms = int(input("Enter the number of terms: "))

    if terms <= 0:
        print("Enter a positive number of terms.")
        return

    print("Square Number Pattern:")

    for i in range(1, terms + 1):
        print(i ** 2, end=" ")

squarenumberpattern()