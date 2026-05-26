def create():
    fingers = ["Thumb", "Index", "Middle", "Ring", "Little"]

    num = int(input("Enter counting number: "))

    position = (num - 1) % 5

    print("Finger =", fingers[position])

create()