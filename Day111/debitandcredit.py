def debtandcredit():
    credit = int(input("Enter total credit: "))
    debt = int(input("Enter total debt: "))

    balance = credit - debt

    print("Net Balance:", balance)

    if balance > 0:
        print("You have more credit than debt.")
    elif balance < 0:
        print("You have more debt than credit.")
    else:
        print("Your credit and debt are equal.")

debtandcredit()