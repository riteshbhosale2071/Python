def divisiontypes(total_items, people, group_size):
    each = total_items // people
    left1 = total_items % people

    groups = total_items // group_size
    left2 = total_items % group_size

    print("\nSharing Division")
    print("Each person gets:", each)
    print("Items left:", left1)

    print("\nGrouping Division")
    print("Total groups:", groups)
    print("Items left:", left2)

items = int(input("Enter total items: "))
people = int(input("Enter number of people: "))
group_size = int(input("Enter group size: "))

divisiontypes(items, people, group_size)