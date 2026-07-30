def fractionequation():
    num1 = int(input("Enter numerator of first fraction: "))
    den1 = int(input("Enter denominator of first fraction: "))

    num2 = int(input("Enter numerator of second fraction: "))
    den2 = int(input("Enter denominator of second fraction: "))

    print("Generated Equation:")
    print(num1, "/", den1, "+", num2, "/", den2, "=",
          num1 * den2 + num2 * den1, "/", den1 * den2)

fractionequation()