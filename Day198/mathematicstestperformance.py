def mathematicstestperformance():
    print("MATHEMATICS TEST PERFORMANCE DASHBOARD :")

    def get_marks(prompt, maximum):
        try:
            marks = float(input(prompt))

            if marks < 0 or marks > maximum:
                print("Marks must be between 0 and", maximum)
                return None

            return marks
        except ValueError:
            print("Invalid input! Enter numeric marks.")
            return None

    try:
        student_count = int(input("Enter the number of students: "))
        subject_count = int(input("Enter the number of mathematics tests: "))
    except ValueError:
        print("Enter valid integer values.")
        return

    if student_count <= 0 or subject_count <= 0:
        print("Students and tests must be greater than zero.")
        return

    student_data = {}
    test_names = []
    maximum_marks = []

    for i in range(subject_count):
        test_name = input(
            "\nEnter test " + str(i + 1) + " name: "
        ).strip()

        if not test_name:
            print("Test name cannot be empty.")
            return

        if test_name.lower() in [name.lower() for name in test_names]:
            print("Test names must be unique.")
            return

        test_names.append(test_name)

        maximum = get_marks(
            "Enter maximum marks for " + test_name + ": ",
            1000000
        )

        if maximum is None or maximum == 0:
            print("Maximum marks must be greater than zero.")
            return

        maximum_marks.append(maximum)

    for i in range(student_count):
        name = input(
            "\nEnter student " + str(i + 1) + " name: "
        ).strip()

        if not name:
            print("Student name cannot be empty.")
            return

        if name.lower() in [student.lower() for student in student_data]:
            print("Student names must be unique.")
            return

        marks_list = []

        for j in range(subject_count):
            marks = get_marks(
                "Enter marks for " + test_names[j] + ": ",
                maximum_marks[j]
            )

            if marks is None:
                return

            marks_list.append(marks)

        student_data[name] = marks_list

    print("PERFORMANCE DASHBOARD :")

    print("\nStudent-Wise Performance :")

    results = {}

    for student, marks_list in student_data.items():
        obtained = sum(marks_list)
        maximum = sum(maximum_marks)
        percentage = obtained / maximum * 100
        average_percentage = sum(
            marks / maximum_marks[i] * 100
            for i, marks in enumerate(marks_list)
        ) / subject_count

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        passed_tests = sum(
            1 for i, marks in enumerate(marks_list)
            if marks / maximum_marks[i] * 100 >= 40
        )

        results[student] = {
            "obtained": obtained,
            "maximum": maximum,
            "percentage": percentage,
            "average_percentage": average_percentage,
            "grade": grade,
            "passed_tests": passed_tests
        }

        print("\nStudent:", student)
        print("Marks:", marks_list)
        print("Total Marks:", obtained, "/", maximum)
        print("Overall Percentage:", round(percentage, 2), "%")
        print("Average Test Percentage:",
              round(average_percentage, 2), "%")
        print("Grade:", grade)
        print("Tests Passed:", passed_tests, "/", subject_count)

    print("\nTest-Wise Performance :")

    for i, test in enumerate(test_names):
        percentages = [
            student_data[student][i] / maximum_marks[i] * 100
            for student in student_data
        ]

        average = sum(percentages) / student_count
        highest = max(percentages)
        lowest = min(percentages)

        top_students = [
            student for student in student_data
            if student_data[student][i] / maximum_marks[i] * 100
            == highest
        ]

        print("\nTest:", test)
        print("Average Percentage:", round(average, 2), "%")
        print("Highest Percentage:", round(highest, 2), "%")
        print("Lowest Percentage:", round(lowest, 2), "%")
        print("Top Performer(s):", ", ".join(top_students))

    print("\nClass Performance Ranking :")

    ranking = sorted(
        results.items(),
        key=lambda item: item[1]["percentage"],
        reverse=True
    )

    for rank, (student, data) in enumerate(ranking, 1):
        print(
            str(rank) + ".",
            student,
            "-",
            round(data["percentage"], 2),
            "%",
            "- Grade",
            data["grade"]
        )

    print("\nOverall Class Statistics :")

    percentages = [
        data["percentage"] for data in results.values()
    ]

    class_average = sum(percentages) / student_count
    highest_percentage = max(percentages)
    lowest_percentage = min(percentages)

    class_pass_count = sum(
        1 for percentage in percentages if percentage >= 40
    )

    class_fail_count = student_count - class_pass_count

    print("Class Average:", round(class_average, 2), "%")
    print("Highest Student Percentage:",
          round(highest_percentage, 2), "%")
    print("Lowest Student Percentage:",
          round(lowest_percentage, 2), "%")
    print("Students Passed Overall:", class_pass_count)
    print("Students Failed Overall:", class_fail_count)
    print("Class Pass Percentage:",
          round(class_pass_count / student_count * 100, 2), "%")

    print("\nPerformance Visualization :")

    for student, data in ranking:
        bar_length = int(data["percentage"] // 5)
        bar = "#" * bar_length

        print(
            student.ljust(20),
            bar,
            str(round(data["percentage"], 2)) + "%"
        )

    print("\nRecommendations :")

    for student, data in results.items():
        if data["percentage"] >= 80:
            print(student + ": Excellent performance. Continue practicing.")
        elif data["percentage"] >= 60:
            print(student + ": Good progress. Focus on weaker topics.")
        elif data["percentage"] >= 40:
            print(student + ": Passed, but additional practice is recommended.")
        else:
            print(student + ": Needs focused revision and extra support.")

    print("\nNote: Overall percentages use total marks obtained divided by")
    print("total maximum marks. Individual test pass status uses 40%.")
    print("\nDashboard generated successfully.")

mathematicstestperformance()