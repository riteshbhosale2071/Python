def anglebisectorproperty():
    print("Angle Bisector Property Calculator")

    a = float(input("Enter side AB: "))
    b = float(input("Enter side AC: "))
    d = float(input("Enter side BD: "))
    e = float(input("Enter side DC: "))

    if min(a, b, d, e) <= 0:
        print("All side lengths must be positive.")
        return

    ratio1 = d / e
    ratio2 = a / b

    print("\nAngle Bisector Property Verification:")
    print("BD / DC =", round(ratio1, 4))
    print("AB / AC =", round(ratio2, 4))

    if abs(ratio1 - ratio2) < 1e-9:
        print("The angle bisector property is verified.")
        print("AD is the angle bisector of angle A.")
    else:
        print("The angle bisector property is not verified.")

    total = d + e
    print("\nLength of BC =", round(total, 4))

    if abs(ratio1 - ratio2) >= 1e-9:
        print("The given side lengths do not satisfy the angle bisector theorem.")

anglebisectorproperty()