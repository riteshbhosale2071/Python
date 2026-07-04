def numberfolding():
    number = input("Enter a number: ")

    print("\nNumber Folding Strip")
    print("-" * 30)

    print("Original :", " ".join(number))

    folded = number[::-1]

    print("Folded   :", " ".join(folded))

    if number == folded:
        print("\nThe number remains the same after folding (Palindrome).")
    else:
        print("\nThe number changes after folding.")

numberfolding()