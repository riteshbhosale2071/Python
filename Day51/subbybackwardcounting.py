def create():
    a = int(input("Enter bigger number: "))
    b = int(input("Enter smaller number: "))

    count = a

    print("\nBackward Counting:")

    while count > a - b:

        count -= 1

        print(count)

    print("\nAnswer =", a - b)

create()