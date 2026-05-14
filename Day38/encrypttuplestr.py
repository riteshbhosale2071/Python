def encrypt():
    t = ("apple", "ball", "cat")
    shift = 2
    encrypted = []

    for word in t:
        new_word = ""

        for ch in word:
            new_word += chr(ord(ch) + shift)

        encrypted.append(new_word)

    result = tuple(encrypted)

    print("Original Tuple:", t)
    print("Encrypted Tuple:", result)

encrypt()