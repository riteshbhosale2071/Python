def color():
    pattern = input("Enter color pattern separated by space : ").split()

    for i in range(len(pattern)):
        if pattern[i] == "?":
            pattern[i] = pattern[i - 2]

    print("Complete Pattern:")
    print(" ".join(pattern))

color()