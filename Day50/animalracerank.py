def find():
    animals = ["Horse", "Dog", "Rabbit", "Cat"]

    times = []

    for i in animals:

        t = int(input(f"Enter time for {i}: "))

        times.append((t, i))

    times.sort()

    print("\nRace Ranking:")

    rank = 1

    for t, i in times:

        print(rank, "->", i)

        rank += 1

find()