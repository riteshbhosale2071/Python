def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def speedratio():
    speed1 = int(input("Enter the first speed: "))
    speed2 = int(input("Enter the second speed: "))

    gcd = find_gcd(speed1, speed2)

    print("Speed Ratio:", speed1, ":", speed2)
    print("Simplified Speed Ratio:", speed1 // gcd, ":", speed2 // gcd)

speedratio()