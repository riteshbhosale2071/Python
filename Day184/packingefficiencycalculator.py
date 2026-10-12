def packingefficiencycalculator():
    print("Packing Efficiency Calculator :")

    container_length = float(input("Enter container length: "))
    container_width = float(input("Enter container width: "))
    container_height = float(input("Enter container height: "))

    box_length = float(input("Enter item length: "))
    box_width = float(input("Enter item width: "))
    box_height = float(input("Enter item height: "))

    if (container_length <= 0 or container_width <= 0 or container_height <= 0
            or box_length <= 0 or box_width <= 0 or box_height <= 0):
        print("All dimensions must be greater than zero.")
        return

    container_volume = container_length * container_width * container_height
    item_volume = box_length * box_width * box_height

    if item_volume > container_volume:
        print("The item is larger than the container by volume.")
        return

    efficiency = (item_volume / container_volume) * 100

    print("\nPacking Efficiency Results :")
    print("Container Volume:", round(container_volume, 2), "cubic units")
    print("Item Volume:", round(item_volume, 2), "cubic units")
    print("Packing Efficiency:", round(efficiency, 2), "%")
    print("Unused Volume:", round(container_volume - item_volume, 2), "cubic units")

    count = int(container_volume // item_volume)
    print("Theoretical Volume-Based Item Count:", count)

    if efficiency == 100:
        print("Result: The item exactly matches the container volume.")
    elif efficiency >= 75:
        print("Result: High volume utilization.")
    elif efficiency >= 40:
        print("Result: Moderate volume utilization.")
    else:
        print("Result: Low volume utilization.")

    print("Note: Actual packing depends on dimensions, orientation, and available space.")

packingefficiencycalculator()