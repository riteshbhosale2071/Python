def statisticsoutlier():
    print("Statistics Outlier Impact Test :")

    n = int(input("Enter the number of observations: "))

    if n < 2:
        print("Enter at least two observations.")
        return

    data = []

    for i in range(n):
        value = float(input("Enter observation " + str(i + 1) + ": "))
        data.append(value)

    original_mean = sum(data) / n
    sorted_data = sorted(data)

    if n % 2 == 1:
        original_median = sorted_data[n // 2]
    else:
        original_median = (
            sorted_data[n // 2 - 1] + sorted_data[n // 2]
        ) / 2

    print("\nOriginal Dataset:", data)
    print("Sorted Dataset:", sorted_data)
    print("Original Mean:", round(original_mean, 2))
    print("Original Median:", round(original_median, 2))
    print("Original Range:", round(max(data) - min(data), 2))

    outlier = float(input("\nEnter the value to test as a potential outlier: "))

    modified_data = data.copy()
    modified_data.append(outlier)

    new_n = len(modified_data)
    new_mean = sum(modified_data) / new_n
    sorted_modified = sorted(modified_data)

    if new_n % 2 == 1:
        new_median = sorted_modified[new_n // 2]
    else:
        new_median = (
            sorted_modified[new_n // 2 - 1] +
            sorted_modified[new_n // 2]
        ) / 2

    new_range = max(modified_data) - min(modified_data)

    print("\nOutlier Impact Results :")
    print("Added Value:", outlier)
    print("Modified Dataset:", modified_data)
    print("New Mean:", round(new_mean, 2))
    print("New Median:", round(new_median, 2))
    print("New Range:", round(new_range, 2))

    print("\nStatistical Changes :")
    print("Mean Change:", round(new_mean - original_mean, 2))
    print("Median Change:", round(new_median - original_median, 2))
    print("Range Change:", round(new_range - (max(data) - min(data)), 2))

    mean_change = abs(new_mean - original_mean)
    median_change = abs(new_median - original_median)
    range_change = abs(new_range - (max(data) - min(data)))

    if mean_change > median_change:
        print("The mean changed more than the median.")
    elif median_change > mean_change:
        print("The median changed more than the mean.")
    else:
        print("The mean and median changed by equal amounts.")

    if outlier > max(data) or outlier < min(data):
        print("The added value lies outside the original data range.")
    else:
        print("The added value lies within the original data range.")

    if range_change > 0:
        print("The range increased after adding the value.")
    else:
        print("The range remained unchanged.")

    print("\nNote: This program measures the impact of an added value.")
    print("It does not statistically confirm whether the value is an outlier.")

statisticsoutlier()