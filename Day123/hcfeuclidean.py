def hcfeuclidean():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    a = abs(a)
    b = abs(b)

    while b != 0:
        remainder = a % b
        print(f"{a} ÷ {b} gives remainder {remainder}")
        a = b
        b = remainder

    print("HCF:", a)

hcfeuclidean()