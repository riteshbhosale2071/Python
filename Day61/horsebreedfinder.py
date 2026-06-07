def horse():
    breed = input("Enter horse height category (small/medium/tall): ").lower()

    if breed == "small":
        print("Breed: Arabian")

    elif breed == "medium":
        print("Breed: Mustang")

    elif breed == "tall":
        print("Breed: Thoroughbred")

    else:
        print("Breed not found")

horse()