def age():
    age = int(input("Enter your age: "))
    if age <= 18:
        print("You are not eligible")
    else:
        print("You are eligible")

age()