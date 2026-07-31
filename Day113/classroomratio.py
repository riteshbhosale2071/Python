def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def classroomratio():
    boys = int(input("Enter the number of boys: "))
    girls = int(input("Enter the number of girls: "))

    gcd = find_gcd(boys, girls)

    print("Total Students:", boys + girls)
    print("Boys : Girls =", boys, ":", girls)
    print("Simplified Ratio =", boys // gcd, ":", girls // gcd)

classroomratio()