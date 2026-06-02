def candy():
    candies = int(input("Enter total candies: "))
    children = int(input("Enter number of children: "))

    each = candies // children
    remaining = candies % children

    print("Each child gets =", each, "candies")
    print("Remaining candies =", remaining)

candy()