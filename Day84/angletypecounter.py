def type():
    n = int(input("Enter number of angles : "))

    acute = 0
    right = 0
    obtuse = 0
    straight = 0
    reflex = 0
    complete = 0

    for i in range(n):
        angle = float(input(f"Enter the angel {i+1} : "))

        if angle > 0 and angle < 90 :
            acute += 1
        elif angle == 90:
            right += 1
        elif angle > 90 and angle < 180 :
            obtuse += 1
        elif angle == 180 :
            straight += 1
        elif angle > 180 and angle < 360 :
            reflex += 1
        elif angle == 360 :
            complete += 1

    print("\nAngle Type Report")
    print("-" * 30)
    print("Acute Angles =", acute)
    print("Right Angles =", right)
    print("Obtuse Angles =", obtuse)
    print("Straight Angles =", straight)
    print("Reflex Angles =", reflex)
    print("Complete Angles =", complete)
        
type()