def multisubjectparticipation():
    print("Multi-Subject Participation :")

    try:
        total_students = int(input("Enter the number of students: "))
        total_subjects = int(input("Enter the number of subjects: "))
    except ValueError:
        print("Invalid input! Enter valid integers.")
        return

    if total_students <= 0 or total_subjects <= 0:
        print("Students and subjects must be greater than zero.")
        return

    students = set()
    subjects = set()
    participation = {}

    for i in range(total_subjects):
        subject = input("Enter subject " + str(i + 1) + ": ").strip()

        if not subject:
            print("Subject name cannot be empty.")
            return

        if subject.lower() in {s.lower() for s in subjects}:
            print("Duplicate subject names are not allowed.")
            return

        subjects.add(subject)

    subject_lookup = {subject.lower(): subject for subject in subjects}

    for i in range(total_students):
        name = input("\nEnter student " + str(i + 1) + " name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            return

        if name.lower() in {s.lower() for s in students}:
            print("Duplicate student names are not allowed.")
            return

        students.add(name)

        try:
            count = int(input("How many subjects did " + name + " participate in? "))
        except ValueError:
            print("Enter a valid integer.")
            return

        if count < 0 or count > total_subjects:
            print("Invalid number of subjects.")
            return

        selected = set()

        for j in range(count):
            subject = input("Enter subject " + str(j + 1) + ": ").strip()

            if subject.lower() not in subject_lookup:
                print("Subject not found in the registered subject list.")
                return

            selected.add(subject_lookup[subject.lower()])

        participation[name] = selected

    print("\n" + "=" * 50)
    print("       PARTICIPATION ANALYSIS REPORT")
    print("=" * 50)

    print("\nRegistered Subjects:", sorted(subjects))
    print("Total Students:", len(students))
    print("Total Subjects:", len(subjects))

    print("\nStudent Participation :")

    for student in sorted(students):
        selected = participation[student]
        print(student, ":", sorted(selected))
        print("Subjects Participated In:", len(selected))
        print("Subjects Not Participated In:",
              sorted(subjects - selected))

    print("\nSubject-Wise Participation :")

    for subject in sorted(subjects):
        participants = {
            student for student in students
            if subject in participation[student]
        }

        print(subject, ":", sorted(participants))
        print("Participant Count:", len(participants))
        print("Participation Percentage:",
              round(len(participants) / len(students) * 100, 2), "%")

    print("\nSet-Based Comparison :")

    active_students = {
        student for student in students
        if participation[student]
    }

    inactive_students = students - active_students

    print("Students Participating in at Least One Subject:",
          sorted(active_students))
    print("Students Not Participating in Any Subject:",
          sorted(inactive_students))

    common_subjects = set.intersection(
        *participation.values()
    ) if participation else set()

    print("Subjects Chosen by Every Student:",
          sorted(common_subjects))

    if len(students) >= 2:
        student_list = sorted(students)
        first_student = student_list[0]
        second_student = student_list[1]

        common = participation[first_student] & participation[second_student]
        different = participation[first_student] ^ participation[second_student]

        print("\nComparison Between", first_student, "and", second_student)
        print("Common Subjects:", sorted(common))
        print("Different Participation:", sorted(different))

    print("\nOverall Statistics :")

    total_participations = sum(
        len(selected) for selected in participation.values()
    )

    possible_participations = len(students) * len(subjects)

    print("Total Recorded Participations:", total_participations)
    print("Possible Participations:", possible_participations)
    print("Overall Participation Percentage:",
          round(total_participations / possible_participations * 100, 2), "%")

    print("\nMulti-subject participation analysis completed successfully.")

multisubjectparticipation()