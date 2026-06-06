def missing():
    alphabets = ['A', 'B', 'C', 'E', 'F']

    for ch in range(ord('A'), ord('F') + 1):

        if chr(ch) not in alphabets:
            print("Missing Alphabet =", chr(ch))

missing()