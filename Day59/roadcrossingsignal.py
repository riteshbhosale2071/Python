def signal():
    signal = input("Enter signal color (Red/Yellow/Green): ").capitalize()

    if signal == "Red":
        print("STOP")

    elif signal == "Yellow":
        print("WAIT")

    elif signal == "Green":
        print("GO")

    else:
        print("Invalid Signal")

signal()