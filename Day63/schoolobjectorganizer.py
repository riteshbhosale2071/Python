def school():
    subjects = input("Enter subject names separated by space: ").split()

    subjects.sort()

    print("Organized Subjects:")

    for subject in subjects:
        print(subject)

school()