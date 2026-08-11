def smallcommonmultiple():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    if not numbers or any(number == 0 for number in numbers):
        print("Please enter non-zero integers.")
        return

    def find_lcm(a, b):
        x, y = abs(a), abs(b)

        while y != 0:
            x, y = y, x % y

        return abs(a * b) // x

    result = abs(numbers[0])

    for number in numbers[1:]:
        result = find_lcm(result, number)

    print("Smallest Common Multiple:", result)

smallcommonmultiple()