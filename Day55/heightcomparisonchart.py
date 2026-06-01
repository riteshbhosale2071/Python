def compare():
    heights = {
        "Ravi": 150,
        "Priya": 160,
        "Amit": 145,
        "Neha": 155
    }

    print("Height Comparison Chart\n")

    for name, height in heights.items():
        print(name, "|" + "*" * (height // 5), height, "cm")

compare()