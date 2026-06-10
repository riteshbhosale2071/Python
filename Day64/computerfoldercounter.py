def folder():
    folders = int(input("Enter number of folders: "))

    total_files = 0

    for i in range(folders):
        files = int(input(f"Enter files in folder {i+1}: "))
        total_files += files

    print("Total Files =", total_files)

folder()