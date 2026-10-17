def classperformancecomparator():
    print("Class Performance Comparator :")

    classes = {}

    class_count = int(input("Enter the number of classes to compare: "))

    if class_count <= 0:
        print("Number of classes must be greater than zero.")
        return

    for i in range(class_count):
        print("\nEnter details for Class", i + 1)

        class_name = input("Enter class name: ")
        n = int(input("Enter the number of students: "))

        if n <= 0:
            print("Number of students must be greater than zero.")
            return

        marks = []

        for j in range(n):
            score = float(input("Enter marks for student " + str(j + 1) + " (0-100): "))

            if score < 0 or score > 100:
                print("Invalid marks! Marks must be between 0 and 100.")
                return

            marks.append(score)

        average = sum(marks) / n
        highest = max(marks)
        lowest = min(marks)
        passed = sum(1 for score in marks if score >= 40)
        pass_percentage = (passed / n) * 100

        classes[class_name] = {
            "students": n,
            "average": average,
            "highest": highest,
            "lowest": lowest,
            "passed": passed,
            "pass_percentage": pass_percentage
        }

    print("\nClass Performance Comparison :")
    print("{:<15} {:<10} {:<12} {:<12} {:<12} {:<12}".format(
        "Class", "Students", "Average", "Highest", "Lowest", "Pass %"
    ))
    print("-" * 75)

    for name, details in classes.items():
        print("{:<15} {:<10} {:<12.2f} {:<12.2f} {:<12.2f} {:<12.2f}".format(
            name,
            details["students"],
            details["average"],
            details["highest"],
            details["lowest"],
            details["pass_percentage"]
        ))

    best_average = max(classes, key=lambda name: classes[name]["average"])
    best_pass_rate = max(classes, key=lambda name: classes[name]["pass_percentage"])
    highest_score_class = max(classes, key=lambda name: classes[name]["highest"])

    print("\nComparison Results :")
    print("Class with Highest Average:", best_average)
    print("Highest Average Marks:", round(classes[best_average]["average"], 2))

    print("\nClass with Best Pass Percentage:", best_pass_rate)
    print("Pass Percentage:", round(classes[best_pass_rate]["pass_percentage"], 2), "%")

    print("\nClass with Highest Individual Score:", highest_score_class)
    print("Highest Score:", classes[highest_score_class]["highest"])

    print("\nOverall Analysis :")

    averages = [details["average"] for details in classes.values()]
    overall_average = sum(averages) / len(averages)

    print("Average of Class Averages:", round(overall_average, 2))

    if len(classes) > 1:
        average_difference = max(averages) - min(averages)
        print("Difference Between Highest and Lowest Class Averages:",
              round(average_difference, 2))

    if average_difference == 0 if len(classes) > 1 else True:
        print("All classes have equal average marks.")
    else:
        print("Class performance varies based on average marks.")

classperformancecomparator()