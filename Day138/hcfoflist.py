def hcfoflist():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    if not numbers or any(number == 0 for number in numbers):
        print("Please enter non-zero integers.")
        return

    def find_hcf(a, b):
        a, b = abs(a), abs(b)

        while b != 0:
            a, b = b, a % b

        return a

    hcf = abs(numbers[0])

    for number in numbers[1:]:
        hcf = find_hcf(hcf, number)

    print("HCF of the List:", hcf)

hcfoflist()