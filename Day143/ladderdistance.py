import math

def ladderdistance():
    ladder_length = float(input("Enter the ladder length: "))
    height = float(input("Enter the height reached by the ladder: "))

    if ladder_length <= 0 or height < 0:
        print("Enter valid positive values.")
        return

    if height > ladder_length:
        print("Height cannot be greater than ladder length.")
        return

    distance_from_wall = math.sqrt(
        ladder_length ** 2 - height ** 2
    )

    print("Distance of Ladder Foot from Wall:", distance_from_wall)

ladderdistance()