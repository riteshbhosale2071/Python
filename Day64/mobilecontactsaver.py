def contact():
    contacts = {}

    name = input("Enter contact name: ")
    number = input("Enter mobile number: ")

    contacts[name] = number

    print("Contact Saved")
    print(contacts)

contact()