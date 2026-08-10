import math

def consecutivecoprime():
    start = int(input("Enter the lower limit: "))
    end = int(input("Enter the upper limit: "))

    all_coprime = True

    for number in range(start, end):
        if math.gcd(number, number + 1) != 1:
            print(f"{number} and {number + 1} are not co-prime.")
            all_coprime = False
        else:
            print(f"{number} and {number + 1} are co-prime.")

    if all_coprime:
        print("\nEvery consecutive pair is co-prime.")
    else:
        print("\nNot every consecutive pair is co-prime.")

consecutivecoprime()