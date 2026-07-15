def arrangeascending():
    num1 = int(input("Enter first large number: "))
    num2 = int(input("Enter second large number: "))
    num3 = int(input("Enter third large number: "))

    numbers = [num1, num2, num3]
    numbers.sort()

    print("Numbers in Ascending Order:")
    for num in numbers:
        print(num)

arrangeascending()