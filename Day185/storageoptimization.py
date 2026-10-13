def storageoptimization():
    print("Storage Optimization :")

    capacity = float(input("Enter total storage capacity in liters: "))
    number = int(input("Enter the number of items to store: "))

    if capacity <= 0 or number <= 0:
        print("Capacity and number of items must be greater than zero.")
        return

    items = []
    total_volume = 0

    for i in range(number):
        print("\nItem", i + 1)

        name = input("Enter item name: ")
        volume = float(input("Enter item volume in liters: "))

        if volume <= 0:
            print("Item volume must be greater than zero.")
            return

        items.append([name, volume])
        total_volume += volume

    items.sort(key=lambda item: item[1])

    print("\nStorage Optimization Report :")
    print("Total Storage Capacity:", round(capacity, 2), "liters")
    print("Total Item Volume:", round(total_volume, 2), "liters")

    if total_volume <= capacity:
        print("All items can fit based on volume.")
        remaining = capacity - total_volume
        print("Remaining Storage:", round(remaining, 2), "liters")
    else:
        print("All items cannot fit in the available storage.")
        excess = total_volume - capacity
        print("Excess Volume:", round(excess, 2), "liters")

    print("\nItems Sorted by Volume :")

    for i in range(number):
        print(
            i + 1, ".",
            items[i][0],
            "-",
            round(items[i][1], 2),
            "liters"
        )

    used_percentage = (total_volume / capacity) * 100

    print("\nStorage Utilization:", round(used_percentage, 2), "%")

    if used_percentage > 100:
        print("Recommendation: Increase storage capacity or remove items.")
    elif used_percentage >= 90:
        print("Recommendation: Storage is nearly full.")
    elif used_percentage >= 50:
        print("Recommendation: Storage is moderately utilized.")
    else:
        print("Recommendation: Plenty of storage space is available.")

    print("Note: This program compares volumes only; actual packing depends on item dimensions.")

storageoptimization()