def verifybetweenness(a, b, c):
    if a < b < c or c < b < a:
        return True
    return False

def main():
    print("Betweenness Verifier")
    print("1. Check whether a number lies between two numbers")
    print("2. Check whether a point lies between two points on a number line")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        a = float(input("Enter the first number: "))
        b = float(input("Enter the number to check: "))
        c = float(input("Enter the third number: "))

        if verifybetweenness(a, b, c):
            print(b, "lies strictly between", a, "and", c)
        else:
            print(b, "does not lie strictly between", a, "and", c)

    elif choice == "2":
        points = []
        n = int(input("Enter the number of points: "))

        if n < 3:
            print("At least three points are required.")
            return

        for i in range(n):
            point = float(input("Enter point " + str(i + 1) + ": "))
            points.append(point)

        a = float(input("Enter the first endpoint: "))
        c = float(input("Enter the second endpoint: "))
        b = float(input("Enter the point to check: "))

        if verifybetweenness(a, b, c):
            print("The point", b, "lies between the endpoints.")
        else:
            print("The point", b, "does not lie between the endpoints.")

    else:
        print("Invalid choice.")

main()