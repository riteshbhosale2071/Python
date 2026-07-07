def distribution(total_items, people):
    each = total_items // people
    left = total_items % people

    print("Each person gets:", each)
    print("Items left:", left)

items = int(input("Enter total items: "))
people = int(input("Enter number of people: "))

distribution(items, people)