def find():
    num = int(input("Enter a 4-digit number: "))
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit ** 4
        num = num // 10
    if temp == sum:
        print("Narcissistic Number")
    else:
        print("Not Narcissistic Number")

find()