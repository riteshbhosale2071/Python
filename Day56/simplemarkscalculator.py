def calc():
    m1 = int(input("Enter marks of Subject 1: "))
    m2 = int(input("Enter marks of Subject 2: "))
    m3 = int(input("Enter marks of Subject 3: "))

    total = m1 + m2 + m3
    percentage = total / 3

    print("Total Marks =", total)
    print("Percentage =", percentage)

calc()