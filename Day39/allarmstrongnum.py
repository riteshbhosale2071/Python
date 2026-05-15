def find():
    t = (153, 370, 123, 407, 200)

    print("Armstrong Numbers:")

    for num in t:
        power = len(str(num))
        total = 0
        n = num

        while n > 0:
            digit = n % 10
            total += digit ** power
            n //= 10

        if total == num:
            print(num)

find()