def cubevolumescaling():
    print("Cube Volume Scaling :")

    side = float(input("Enter the original cube side length: "))
    scale_factor = float(input("Enter the scaling factor: "))

    if side <= 0 or scale_factor <= 0:
        print("Side length and scaling factor must be greater than zero.")
        return

    original_volume = side ** 3
    new_side = side * scale_factor
    new_volume = new_side ** 3

    volume_ratio = new_volume / original_volume
    volume_increase = new_volume - original_volume
    percentage_change = ((new_volume - original_volume) / original_volume) * 100

    print("\nVolume Scaling Results :")
    print("Original Side Length:", round(side, 2))
    print("Scaled Side Length:", round(new_side, 2))
    print("Original Volume:", round(original_volume, 2))
    print("Scaled Volume:", round(new_volume, 2))
    print("Volume Scaling Ratio:", round(volume_ratio, 2))
    print("Volume Difference:", round(volume_increase, 2))
    print("Percentage Change:", round(percentage_change, 2), "%")

    if scale_factor > 1:
        print("Result: The cube's volume increased.")
    elif scale_factor < 1:
        print("Result: The cube's volume decreased.")
    else:
        print("Result: The cube's volume remained unchanged.")

cubevolumescaling()