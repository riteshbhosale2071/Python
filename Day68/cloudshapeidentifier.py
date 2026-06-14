def cloud():
    shape = input("Enter cloud shape (round/long/fluffy): ").lower()

    if shape == "round":
        print("Cloud looks like a Balloon")

    elif shape == "long":
        print("Cloud looks like a Snake")

    elif shape == "fluffy":
        print("Cloud looks like a Sheep")

    else:
        print("Unknown Cloud Shape")

cloud()