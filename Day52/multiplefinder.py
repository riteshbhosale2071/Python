def find():
    num = int(input("Enter number: "))
    
    limit = int(input("Enter limit: "))

    print("Multiples are:")

    for i in range(1, limit + 1):
        print(num * i)

find()