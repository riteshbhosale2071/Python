def rank():
    n = int(input("Enter number of objects: "))

    objects = []

    for i in range(n):
        names = input("Enter the name of object: ")
        length = float(input("Enter the length of object: "))
        objects.append((names,length))

    objects.sort(key = lambda x:x[1])

    print("Ranking of objects is")
    for i in objects:
        print(i)
        
rank()