def multiple():
    n = int(input("Enter number of lengths:"))

    lengths = []
    
    for i in range(n):
        length = float(input(f"Enter the length {i+1}:"))
        lengths.append(length)

    print("Longest length is",max(lengths))
    print("Smallest length is",min(lengths))

multiple()