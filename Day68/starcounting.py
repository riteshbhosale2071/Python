def star():
    nights = int(input("Enter number of nights: "))

    total_stars = 0

    for i in range(nights):
        stars = int(input(f"Enter stars counted on night {i+1}: "))
        total_stars += stars

    print("Total Stars Counted =", total_stars)

star()