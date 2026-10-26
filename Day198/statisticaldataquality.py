def statisticaldataquality():
    print("Statistical Data Quality Checker :")

    def read_number(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            return None

    try:
        count = int(input("Enter the number of data values: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if count <= 0:
        print("The number of data values must be greater than zero.")
        return

    data = []
    missing_count = 0

    print("\nEnter data values.")
    print("Use M to represent a missing value.")

    for i in range(count):
        value = input("Enter value " + str(i + 1) + ": ").strip()

        if value.lower() == "m":
            data.append(None)
            missing_count += 1
        else:
            try:
                number = float(value)
                data.append(number)
            except ValueError:
                print("Invalid value. Enter a number or M.")
                return

    valid_data = [value for value in data if value is not None]

    print("\n" + "=" * 45)
    print("       DATA QUALITY REPORT")
    print("=" * 45)

    print("\nTotal Records:", count)
    print("Valid Records:", len(valid_data))
    print("Missing Records:", missing_count)

    missing_percentage = missing_count / count * 100
    print("Missing Data Percentage:", round(missing_percentage, 2), "%")

    if valid_data:
        print("\nDescriptive Statistics :")

        total = sum(valid_data)
        mean = total / len(valid_data)
        minimum = min(valid_data)
        maximum = max(valid_data)
        data_range = maximum - minimum

        sorted_data = sorted(valid_data)
        n = len(sorted_data)

        if n % 2 == 0:
            median = (
                sorted_data[n // 2 - 1] + sorted_data[n // 2]
            ) / 2
        else:
            median = sorted_data[n // 2]

        variance = sum((value - mean) ** 2 for value in valid_data) / n
        standard_deviation = variance ** 0.5

        print("Minimum:", minimum)
        print("Maximum:", maximum)
        print("Range:", data_range)
        print("Mean:", round(mean, 2))
        print("Median:", round(median, 2))
        print("Population Variance:", round(variance, 2))
        print("Population Standard Deviation:",
              round(standard_deviation, 2))

        print("\nDuplicate Detection :")

        duplicates = []
        seen = set()

        for value in valid_data:
            if value in seen and value not in duplicates:
                duplicates.append(value)
            seen.add(value)

        if duplicates:
            print("Duplicate Values:", sorted(duplicates))
        else:
            print("No duplicate values found.")

        print("\nOutlier Detection :")

        if n >= 4:
            def find_median(values):
                length = len(values)

                if length % 2 == 0:
                    return (
                        values[length // 2 - 1] + values[length // 2]
                    ) / 2

                return values[length // 2]

            lower_half = sorted_data[:n // 2]
            upper_half = sorted_data[(n + 1) // 2:]

            q1 = find_median(lower_half)
            q3 = find_median(upper_half)
            iqr = q3 - q1

            lower_limit = q1 - 1.5 * iqr
            upper_limit = q3 + 1.5 * iqr

            outliers = [
                value for value in valid_data
                if value < lower_limit or value > upper_limit
            ]

            print("First Quartile (Q1):", round(q1, 2))
            print("Third Quartile (Q3):", round(q3, 2))
            print("Interquartile Range:", round(iqr, 2))
            print("Lower Limit:", round(lower_limit, 2))
            print("Upper Limit:", round(upper_limit, 2))

            if outliers:
                print("Potential Outliers:", sorted(outliers))
            else:
                print("No potential outliers detected.")
        else:
            print("At least four valid values are needed for this check.")

        print("\nData Consistency Checks :")

        if minimum == maximum:
            print("Warning: All valid values are identical.")
        else:
            print("Variation detected in the dataset.")

        if any(value < 0 for value in valid_data):
            print("Note: Negative values exist; verify they are permitted.")
        else:
            print("No negative values detected.")

        if missing_count == 0:
            print("Missing-value check: Passed.")
        else:
            print("Missing-value check: Review missing records.")

        print("\nData Quality Assessment :")

        quality_score = 100 - missing_percentage

        if duplicates:
            quality_score -= 5

        if n >= 4 and outliers:
            quality_score -= min(15, len(outliers) * 3)

        quality_score = max(0, quality_score)

        print("Estimated Quality Score:",
              round(quality_score, 2), "%")

        if quality_score >= 90:
            print("Assessment: Good data quality.")
        elif quality_score >= 70:
            print("Assessment: Moderate data quality.")
        else:
            print("Assessment: Data requires review and cleaning.")

    else:
        print("\nNo valid numerical values are available for analysis.")

    print("\nFinal Validation :")

    if len(valid_data) + missing_count == count:
        print("Record count verification: Passed.")
    else:
        print("Record count verification: Failed.")

    print("Data quality analysis completed.")

statisticaldataquality()