def platform():
    trains = {
        "Express": 1,
        "Rajdhani": 2,
        "Shatabdi": 3,
        "Local": 4
    }

    train = input("Enter train name: ").capitalize()

    if train in trains:
        print("Platform Number =", trains[train])
    else:
        print("Train not found")

platform()