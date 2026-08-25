def hcfbasedgrouping():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    if not numbers or any(number == 0 for number in numbers):
        print("Please enter non-zero integers.")
        return

    def find_hcf(a, b):
        a, b = abs(a), abs(b)

        while b != 0:
            a, b = b, a % b

        return a

    groups = {}

    for number in numbers:
        hcf = find_hcf(abs(numbers[0]), abs(number))

        if hcf not in groups:
            groups[hcf] = []

        groups[hcf].append(number)

    print("\nHCF-Based Groups:")

    for hcf, group in groups.items():
        print(f"HCF {hcf}: {group}")

hcfbasedgrouping()