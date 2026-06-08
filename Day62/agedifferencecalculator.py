def age():
    age1 = int(input("Enter first person's age: "))
    
    age2 = int(input("Enter second person's age: "))

    difference = abs(age1 - age2)

    print("Age Difference =", difference, "years")

age()