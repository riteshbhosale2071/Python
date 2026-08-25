def runninglcm():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    if not numbers or any(number == 0 for number in numbers):
        print("Please enter non-zero integers.")
        return

    def find_hcf(a, b):
        a, b = abs(a), abs(b)

        while b != 0:
            a, b = b, a % b

        return a

    def find_lcm(a, b):
        return abs(a * b) // find_hcf(a, b)

    current_lcm = abs(numbers[0])

    print("Running LCM:")

    for i, number in enumerate(numbers):
        if i == 0:
            current_lcm = abs(number)
        else:
            current_lcm = find_lcm(current_lcm, number)

        print(f"After {i + 1} number(s): {current_lcm}")

runninglcm()