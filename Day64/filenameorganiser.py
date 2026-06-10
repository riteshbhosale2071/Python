def file():
    files = input("Enter file names separated by space: ").split()

    files.sort()

    print("Organized File Names:")

    for file in files:
        print(file)

file()