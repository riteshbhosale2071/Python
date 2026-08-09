def missinginteger():
    sequence = input("Enter integers separated by spaces: ").split()
    numbers = [int(x) for x in sequence]

    min_num = min(numbers)
    max_num = max(numbers)

    missing = []

    for num in range(min_num, max_num + 1):
        if num not in numbers:
            missing.append(num)

    if missing:
        print("Missing Integer(s):", missing)
    else:
        print("No integer is missing.")

missinginteger()