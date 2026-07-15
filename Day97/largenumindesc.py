def arrangedescending():
    num1 = int(input("Enter first large number: "))
    num2 = int(input("Enter second large number: "))
    num3 = int(input("Enter third large number: "))

    numbers = [num1, num2, num3]
    numbers.sort(reverse=True)

    print("Numbers in Descending Order:")
    for num in numbers:
        print(num)

arrangedescending()