def rev():
    string = input("Enter a string: ")

    words = string.split()

    reverse_words = words[::-1]

    result = " ".join(reverse_words)

    print("Reversed String =", result)

rev()