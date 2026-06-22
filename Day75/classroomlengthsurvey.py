def classroom():
    count = int(input("Enter number of classroom:"))

    lengths = []
    
    for i in range(count):
        length = float(input(f"Enter the length of classroom {i+1} (meters):"))
        lengths.append(length)

    print("Maximum length of classroom is",max(lengths),"meters")
    print("Minimum length of classroom is",min(lengths),"meters")
    print("Average length of classroom is",sum(lengths)/len(lengths),"meters")

classroom()