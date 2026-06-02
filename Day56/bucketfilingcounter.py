def bucket():
    bucket_capacity = int(input("Enter bucket capacity (litres): "))
    fill_per_turn = int(input("Water added each time (litres): "))

    water = 0
    count = 0

    while water < bucket_capacity:

        water += fill_per_turn
        count += 1

        if water > bucket_capacity:
            water = bucket_capacity

        print("Water in Bucket =", water)

    print("\nBucket Full!")
    print("Total Fillings =", count)

bucket()