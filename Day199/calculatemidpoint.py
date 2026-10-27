def calculatemidpoint(x1, y1, x2, y2):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return mid_x, mid_y

def calculate3dmidpoint(x1, y1, z1, x2, y2, z2):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    mid_z = (z1 + z2) / 2
    return mid_x, mid_y, mid_z

def main():
    print("Midpoint Calculator")
    print("1. Midpoint in 2D")
    print("2. Midpoint in 3D")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        midpoint = calculatemidpoint(x1, y1, x2, y2)
        print("Midpoint:", midpoint)

    elif choice == "2":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))

        midpoint = calculate3dmidpoint(x1, y1, z1, x2, y2, z2)
        print("Midpoint:", midpoint)

    else:
        print("Invalid choice.")

main()