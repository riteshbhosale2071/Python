phonebook = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact added!")

    elif choice == 2:
        name = input("Enter name to search: ")
        if name in phonebook:
            print("Phone number:", phonebook[name])
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter name to delete: ")
        if name in phonebook:
            phonebook.pop(name)
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == 4:
        print("\nPhonebook:")
        for name, number in phonebook.items():
            print(name, ":", number)

    elif choice == 5:
        print("Exiting")
        break

    else:
        print("Invalid choice")