def fruit():
    n = int(input("Enter number of students: "))

    fruits = {}

    for i in range(n):
        fruit = input(f"Enter favourite fruit of student {i+1}: ").capitalize()

        if fruit in fruits:
            fruits[fruit] += 1
        else:
            fruits[fruit] = 1

    print("\nSurvey Result")
    print("-" * 30)

    for fruit, count in fruits.items():
        print(fruit, ":", count)

    favourite = max(fruits, key=fruits.get)

    print("\nMost Favourite Fruit =", favourite)
    print("Votes =", fruits[favourite])

fruit()