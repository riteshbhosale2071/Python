def equal():
    items = int(input("Enter total items: "))
    people = int(input("Enter number of people: "))

    share = items // people
    remaining = items % people

    print("Each person gets =", share)
    print("Remaining items =", remaining)

equal()