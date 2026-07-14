def expandedform():
    number = input("Enter an 8-digit number: ")

    if len(number) == 8:
        print("Expanded Form:")
        print(number[0] + "0000000 +",
              number[1] + "000000 +",
              number[2] + "00000 +",
              number[3] + "0000 +",
              number[4] + "000 +",
              number[5] + "00 +",
              number[6] + "0 +",
              number[7])
    else:
        print("Please enter an 8-digit number.")

expandedform()