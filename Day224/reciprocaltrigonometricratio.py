import math

def reciprocaltrigonometricratio():
    print("Reciprocal Trigonometric Ratio Calculator")
    print("1. Calculate Cosec")
    print("2. Calculate Sec")
    print("3. Calculate Cot")
    print("4. Calculate All Reciprocal Ratios")

    choice = input("Enter your choice (1-4): ")

    angle = float(input("Enter angle in degrees: "))
    radian = math.radians(angle)

    sine = math.sin(radian)
    cosine = math.cos(radian)

    cosec = None if math.isclose(sine, 0, abs_tol=1e-10) else 1 / sine
    sec = None if math.isclose(cosine, 0, abs_tol=1e-10) else 1 / cosine
    cot = None if math.isclose(sine, 0, abs_tol=1e-10) else cosine / sine

    if choice == "1":
        print("Cosec =", "Undefined" if cosec is None else round(cosec, 4))

    elif choice == "2":
        print("Sec =", "Undefined" if sec is None else round(sec, 4))

    elif choice == "3":
        print("Cot =", "Undefined" if cot is None else round(cot, 4))

    elif choice == "4":
        print("Cosec =", "Undefined" if cosec is None else round(cosec, 4))
        print("Sec =", "Undefined" if sec is None else round(sec, 4))
        print("Cot =", "Undefined" if cot is None else round(cot, 4))

    else:
        print("Invalid choice.")

reciprocaltrigonometricratio()