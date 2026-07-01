import random

def arithmetic():
    problem = random.randint(1, 5)

    if problem == 1:
        a = random.randint(5, 20)
        b = random.randint(5, 20)
        print(f"Riya has {a} apples. She buys {b} more apples.")
        print("Question: How many apples does she have now?")
        print("Answer =", a + b)

    elif problem == 2:
        a = random.randint(20, 50)
        b = random.randint(5, a)
        print(f"Rahul had ₹{a}. He spent ₹{b}.")
        print("Question: How much money is left?")
        print("Answer = ₹", a - b)

    elif problem == 3:
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        print(f"There are {a} boxes with {b} chocolates in each box.")
        print("Question: How many chocolates are there in total?")
        print("Answer =", a * b)

    elif problem == 4:
        a = random.randint(2, 8)
        b = random.randint(10, 50)
        print(f"A rope is {b} metres long. It is cut into {a} equal pieces.")
        print("Question: What is the length of each piece?")
        print("Answer =", round(b / a, 2), "metres")

    else:
        a = random.randint(2, 8)
        b = random.randint(5, 20)
        print(f"One notebook costs ₹{b}. Aman buys {a} notebooks.")
        print("Question: How much money does he pay?")
        print("Answer = ₹", a * b)


arithmetic()