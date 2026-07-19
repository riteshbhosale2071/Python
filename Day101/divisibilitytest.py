def divisibilitytest():
    number = int(input("Enter a number: "))
    divisor = int(input("Enter divisor: "))

    if number % divisor == 0:
        print(number, "is divisible by", divisor)
    else:
        print(number, "is not divisible by", divisor)

divisibilitytest()