def indexvaluecalc():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    index = int(input("Enter the index: "))

    if 0 <= index < len(numbers):
        print("Value at Index:", numbers[index])
    else:
        print("Invalid index.")

indexvaluecalc()