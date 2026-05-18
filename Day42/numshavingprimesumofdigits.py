def find():
    t = (23, 44, 56, 71)

    for num in t:
        digit_sum = sum(int(d) for d in str(num))

        prime = True

        if digit_sum < 2:
            prime = False

        for i in range(2, digit_sum):

            if digit_sum % i == 0:
                prime = False
                break

        if prime:
            print(num)

find()