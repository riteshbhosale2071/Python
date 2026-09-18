def pipefillingvariation():
    print("Pipe-Filling Variation Simulator :")
    print("1. One pipe")
    print("2. Multiple pipes")

    choice = int(input("Enter choice: "))

    if choice == 1:
        flow_rate = float(input("Enter flow rate (litres/min): "))
        capacity = float(input("Enter tank capacity (litres): "))

        if flow_rate > 0:
            time = capacity / flow_rate
            print("Filling time =", time, "minutes")
        else:
            print("Flow rate must be greater than zero.")

    elif choice == 2:
        pipe1 = float(input("Enter flow rate of pipe 1: "))
        pipe2 = float(input("Enter flow rate of pipe 2: "))
        capacity = float(input("Enter tank capacity (litres): "))

        total_rate = pipe1 + pipe2

        if total_rate > 0:
            time = capacity / total_rate
            print("Combined flow rate =", total_rate, "litres/min")
            print("Filling time =", time, "minutes")
        else:
            print("Total flow rate must be greater than zero.")

    else:
        print("Invalid choice.")

pipefillingvariation()