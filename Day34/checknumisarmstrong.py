def check():
    num = int(input("Enter a number: "))
    temp = num
    sum = 0
    n = len(str(num))
    while num > 0:
        digit = num % 10
        sum = sum + digit ** n
        num = num // 10
    if temp == sum:
        print("Armstrong Number")
    else:
        print("Not Armstrong Number")

check()