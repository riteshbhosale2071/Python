def distribution():
    weight = float(input("Enter total weight (kg) :"))
    
    persons = int(input("Enter total persons :"))

    distribution = weight / persons

    print("Distribution of weight to per person is",distribution)

distribution()