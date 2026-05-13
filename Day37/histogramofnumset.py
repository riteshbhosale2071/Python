def find():
    numbers = [2, 5, 7, 12, 15, 18, 22, 25, 27]

    bin_size = int(input("Enter bin size: "))

    histogram = {}

    for num in numbers:

        bin_start = (num // bin_size) * bin_size
        bin_end = bin_start + bin_size - 1

        key = f"{bin_start}-{bin_end}"

        if key in histogram:
            histogram[key] += 1
        else:
            histogram[key] = 1

    print(histogram)

find()