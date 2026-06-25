def shape():
    pattern = input("Enter shapes separated by space (use ? for missing): ").split()

    for i in range(len(pattern)):
        if pattern[i] == "?":
            pattern[i] = pattern[i - 1]

    print("Completed Pattern:")
    print(" ".join(pattern))

shape()