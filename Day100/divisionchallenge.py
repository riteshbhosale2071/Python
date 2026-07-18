import random

def divisionchallenge():
    divisor = random.randint(2, 10)
    quotient = random.randint(2, 20)

    dividend = divisor * quotient

    print("Division Challenge")
    print("Find the quotient:")
    print(dividend, "÷", divisor)

    answer = int(input("Enter your answer: "))

    if answer == quotient:
        print("Correct!")
    else:
        print("Wrong! Correct Answer =", quotient)

divisionchallenge()