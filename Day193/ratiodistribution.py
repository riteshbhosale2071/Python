def ratiodistribution():
    print("Ratio Distribution :")

    try:
        n = int(input("Enter the number of people or groups: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of people or groups must be greater than zero.")
        return

    names = []
    ratios = []

    for i in range(n):
        name = input("Enter name of person/group " + str(i + 1) + ": ")

        try:
            ratio = float(input("Enter ratio value for " + name + ": "))
        except ValueError:
            print("Invalid ratio value!")
            return

        if ratio < 0:
            print("Ratio values cannot be negative.")
            return

        names.append(name)
        ratios.append(ratio)

    total_amount = float(input("\nEnter the total amount to distribute: "))

    if total_amount < 0:
        print("Total amount cannot be negative.")
        return

    total_ratio = sum(ratios)

    if total_ratio == 0:
        print("Cannot distribute because the total ratio is zero.")
        return

    print("\nDistribution Results :")
    print("Total Amount:", total_amount)
    print("Total Ratio:", total_ratio)

    distributed_amounts = []

    for i in range(n):
        share = (ratios[i] / total_ratio) * total_amount
        distributed_amounts.append(share)

        percentage = (ratios[i] / total_ratio) * 100

        print("\nName:", names[i])
        print("Ratio:", ratios[i])
        print("Share:", round(share, 2))
        print("Distribution Percentage:", round(percentage, 2), "%")

    print("\nDistribution Summary :")
    print("Total Distributed:", round(sum(distributed_amounts), 2))
    print("Undistributed Amount:",
          round(total_amount - sum(distributed_amounts), 2))

    largest_index = ratios.index(max(ratios))
    smallest_index = ratios.index(min(ratios))

    print("Largest Ratio Share:", names[largest_index])
    print("Smallest Ratio Share:", names[smallest_index])

    print("\nVerification :")

    for i in range(n):
        print(
            names[i] + ":",
            round(distributed_amounts[i], 2),
            "based on ratio",
            ratios[i]
        )

    if abs(sum(distributed_amounts) - total_amount) < 0.01:
        print("Verification successful: The total amount is distributed.")
    else:
        print("Verification note: A small rounding difference may exist.")

ratiodistribution()