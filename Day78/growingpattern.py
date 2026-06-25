def growing():
    start = int(input("Enter the starting number : "))
    difference = int(input("Enter the difference : "))
    terms = int(input("Enter number of terms : "))

    for i in range(terms):
        print(start + i * difference,end = " ")

growing()