# Problem Statement: Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
# n will be provided by the user

def find():
    n = int(input("Enter value of n: "))
    sum = 0
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        sum = sum + (i / fact)

    print("Sum of series =", sum)

find()