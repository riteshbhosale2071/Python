def value():
    number = int(input("Enter a 3-digit number: "))

    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10

    print("Hundreds Place Value =", hundreds * 100)
    print("Tens Place Value =", tens * 10)
    print("Ones Place Value =", ones)

value()