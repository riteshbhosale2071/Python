def farm():
    animals = ["cow", "goat", "cow", "hen", "goat", "sheep"]

    cow_group = []
    goat_group = []
    hen_group = []
    sheep_group = []

    for animal in animals:

        if animal == "cow":
            cow_group.append(animal)

        elif animal == "goat":
            goat_group.append(animal)

        elif animal == "hen":
            hen_group.append(animal)

        elif animal == "sheep":
            sheep_group.append(animal)

    print("Cows :", cow_group)
    print("Goats:", goat_group)
    print("Hens :", hen_group)
    print("Sheep:", sheep_group)

farm()