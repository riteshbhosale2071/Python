def show():

    start = int(input("Enter starting number: "))

    end = int(input("Enter ending number: "))

    for i in range(start, end + 1, 10):
        
        print(i)

show()