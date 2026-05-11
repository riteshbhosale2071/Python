def find():
    string = input("Enter a string: ")
    char = input("Enter character to find: ")

    index = string.find(char)

    if index != -1:
        print("Character found at index:", index)
    else:
        print("Character not found")

find()