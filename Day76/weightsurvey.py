def survey():
    n = int(input("Enter number of persons:"))

    weight = []
    
    for i in range(n):
        weights = float(input(f"Enter the weight of person {i+1} (kg):"))
        weight.append(weights)

    average = sum(weight) / len(weight)

    print("Average weight of persons is",round(average),"kg")

survey()