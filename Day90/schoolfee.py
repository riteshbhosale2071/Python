def schoolfee():
    tuition_fee = float(input("Enter tuition fee: "))
    bus_fee = float(input("Enter bus fee: "))
    exam_fee = float(input("Enter exam fee: "))

    total_fee = tuition_fee + bus_fee + exam_fee

    print("Total School Fee:", total_fee)

schoolfee()