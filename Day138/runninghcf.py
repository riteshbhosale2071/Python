def runninghcf():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    if not numbers or any(number == 0 for number in numbers):
        print("Please enter non-zero integers.")
        return

    def find_hcf(a, b):
        a, b = abs(a), abs(b)

        while b != 0:
            a, b = b, a % b

        return a

    current_hcf = abs(numbers[0])

    print("Running HCF:")

    for i, number in enumerate(numbers):
        if i == 0:
            current_hcf = abs(number)
        else:
            current_hcf = find_hcf(current_hcf, number)

        print(f"After {i + 1} number(s): {current_hcf}")

runninghcf()