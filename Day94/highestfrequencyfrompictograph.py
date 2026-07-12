def highestfrequency():
    item1 = input("Enter first item: ")
    count1 = int(input("Enter frequency of first item: "))

    item2 = input("Enter second item: ")
    count2 = int(input("Enter frequency of second item: "))

    if count1 > count2:
        print("Highest Frequency:", item1)
    elif count2 > count1:
        print("Highest Frequency:", item2)
    else:
        print("Both items have the same frequency.")

highestfrequency()