def find():
    t = (12, 4567, 89, 123456, 90)

    max_digits = 0
    result = 0

    for num in t:
        digits = len(str(num))

        if digits > max_digits:
            max_digits = digits
            result = num

    print("Element with Maximum Digits:", result)

find()