def oppositenumber():
    numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

    opposites = [-num for num in numbers]

    print("Original Numbers:", numbers)
    print("Opposite Numbers:", opposites)

oppositenumber()