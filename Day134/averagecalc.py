def averagecalc():
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

    if not numbers:
        print("Please enter at least one number.")
        return

    average = sum(numbers) / len(numbers)

    print("Average:", average)

averagecalc()