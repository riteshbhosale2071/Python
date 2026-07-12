def pictographcomparison():
    item1 = input("Enter first item: ")
    count1 = int(input("Enter frequency of first item: "))

    item2 = input("Enter second item: ")
    count2 = int(input("Enter frequency of second item: "))

    if count1 > count2:
        print(item1, "has more symbols.")
    elif count2 > count1:
        print(item2, "has more symbols.")
    else:
        print("Both have the same number of symbols.")

pictographcomparison()