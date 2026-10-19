def numberlineposition():
    print("Number Line Position :")

    try:
        number = float(input("Enter a number: "))
        reference = float(input("Enter the reference point: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    position = number - reference

    print("\nPosition Analysis :")
    print("Given Number:", number)
    print("Reference Point:", reference)
    print("Position Difference:", round(position, 4))

    if number < reference:
        print("Position: The number is to the left of the reference point.")
        print("Distance:", round(reference - number, 4))
    elif number > reference:
        print("Position: The number is to the right of the reference point.")
        print("Distance:", round(number - reference, 4))
    else:
        print("Position: The number is exactly at the reference point.")
        print("Distance: 0")

    print("\nNumber Classification :")

    if number == 0:
        print("The number is zero.")
    elif number > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")

    if number == int(number):
        print("Number Type: Integer")
    else:
        print("Number Type: Decimal")

    print("\nNumber Line Representation :")

    if number == reference:
        print("Reference Point:", reference, "<-- Given Number")
    elif number < reference:
        print(number, "<----------------", reference)
        print("Given Number is on the left.")
    else:
        print(reference, "---------------->", number)
        print("Given Number is on the right.")

    print("\nAbsolute Distance:", round(abs(number - reference), 4))

numberlineposition()