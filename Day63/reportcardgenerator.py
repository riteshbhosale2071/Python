def reportcard():
    name = input("Enter student name: ")

    m1 = float(input("Enter Math marks: "))
    m2 = float(input("Enter Science marks: "))
    m3 = float(input("Enter English marks: "))

    total = m1 + m2 + m3
    average = total / 3

    print("\nREPORT CARD")
    print("Name:", name)
    print("Math:", m1)
    print("Science:", m2)
    print("English:", m3)
    print("Total:", total)
    print("Average:", average)

reportcard()