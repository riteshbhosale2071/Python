import math
def find():
    r = float(input("Enter radius of cylinder: "))
    h = float(input("Enter height of cylinder: "))

    volume = math.pi * r * r * h

    cost = volume * 40

    print("Volume of cylinder =", volume)
    print("Cost of milk =", cost)

find()