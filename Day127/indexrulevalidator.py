def indexrulevalidator():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    index = int(input("Enter the index: "))

    if 0 <= index < len(numbers):
        expected_value = index + 1

        if numbers[index] == expected_value:
            print("The index rule is valid.")
        else:
            print("The index rule is not valid.")
            print("Expected value:", expected_value)
    else:
        print("Invalid index.")

indexrulevalidator()