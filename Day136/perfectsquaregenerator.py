def perfectsquaregenerator():
    limit = int(input("Enter the limit: "))

    if limit < 1:
        print("Enter a positive limit.")
        return

    print("Perfect Squares:")

    number = 1

    while number ** 2 <= limit:
        print(number ** 2, end=" ")
        number += 1

perfectsquaregenerator()