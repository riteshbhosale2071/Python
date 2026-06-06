def length():
    word = input("Enter a word: ")

    length = len(word)

    if length <= 3:
        print("Short Word")

    elif length <= 7:
        print("Medium Word")

    else:
        print("Long Word")

length()