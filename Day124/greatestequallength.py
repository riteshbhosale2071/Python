def greatestequallength():
    lengths = list(map(int, input("Enter lengths separated by spaces: ").split()))

    if not lengths or any(length <= 0 for length in lengths):
        print("Please enter positive lengths.")
        return

    def find_hcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    greatest_length = lengths[0]

    for length in lengths[1:]:
        greatest_length = find_hcf(greatest_length, length)

    print("Greatest Equal Length:", greatest_length)

greatestequallength()