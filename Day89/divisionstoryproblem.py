def divisionstory(total_items, people):
    quotient = total_items // people
    remainder = total_items % people

    print("\nStory Problem:")
    print("There are", total_items, "chocolates shared among", people, "children.")
    print("Each child gets", quotient, "chocolates.")
    print("Chocolates left:", remainder)

items = int(input("Enter total items: "))
people = int(input("Enter number of people: "))

divisionstory(items, people)