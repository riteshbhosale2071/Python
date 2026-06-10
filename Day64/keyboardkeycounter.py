def keyboard():
    text = input("Type something: ")

    letters = 0
    digits = 0
    spaces = 0

    for ch in text:

        if ch.isalpha():
            letters += 1

        elif ch.isdigit():
            digits += 1

        elif ch == " ":
            spaces += 1

    print("Letters =", letters)
    print("Digits =", digits)
    print("Spaces =", spaces)

keyboard()