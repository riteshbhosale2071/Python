def zoo():
    animals = input("Enter animal names: ").split()

    count = {}

    for animal in animals:

        if animal in count:
            count[animal] += 1

        else:
            count[animal] = 1

    print(count)

zoo()