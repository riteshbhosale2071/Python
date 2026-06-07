def generate():
    name = input("Enter full name: ")

    words = name.split()

    for word in words:
        print(word[0].upper(), end=".")

generate()