def comparison():
    n = int(input("Enter number of objects : "))

    weight = []

    for i in range(n):
        name = input("Enter the name of object : ")
        weights = float(input("Enter the weight of object (kg) : "))
        weight.append((name,weights))
    
    print("\nWeight Comparison Table")
    print("-"*30)
    print("Object\t\tWeight(Kg)")
    print("-"*30)

    for item in weight:
        print(item[0],"\t\t",item[1])
comparison()