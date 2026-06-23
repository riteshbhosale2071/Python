def heaviest():
    n = int(input("Enter number of items : "))

    heaviestname = ""
    heaviestweight = 0

    for i in range(n):
        name = input("Enter name of item : ")
        weight = float(input("Enter weight of item (kg) : "))

        if weight > heaviestweight:
            heaviestweight = weight
            heaviestname = name

    print("\nHeaviest Item name is",heaviestname)
    print("Heaviest Item weight is",heaviestweight)

heaviest()