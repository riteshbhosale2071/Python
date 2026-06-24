def ranking():
    n = int(input("Enter number of containers: "))

    containers = []

    for i in range(n):
        name = input("Enter container name: ")
        capacity = float(input("Enter capacity (liters): "))

        containers.append((name, capacity))

    containers.sort(key=lambda x: x[1], reverse=True)

    print("\nCapacity Ranking")
    print("-" * 30)

    for rank, (name, capacity) in enumerate(containers, start=1):
        print(f"{rank}. {name} - {capacity} liters")

ranking()