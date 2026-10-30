def triangleproportionality():
    print("Triangle Proportionality Checker")
    print("1. Check proportional sides")
    print("2. Find missing proportional side")
    print("3. Check Basic Proportionality Theorem")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first side of triangle 1: "))
        b = float(input("Enter corresponding side of triangle 1: "))
        c = float(input("Enter first side of triangle 2: "))
        d = float(input("Enter corresponding side of triangle 2: "))

        if a > 0 and b > 0 and c > 0 and d > 0:
            if abs((a / b) - (c / d)) < 0.000001:
                print("The sides are proportional.")
            else:
                print("The sides are not proportional.")
        else:
            print("Side lengths must be positive.")

    elif choice == "2":
        a = float(input("Enter first known side: "))
        b = float(input("Enter corresponding side: "))
        c = float(input("Enter second known side: "))

        if a > 0 and b > 0 and c > 0:
            missing = (b * c) / a
            print("Missing proportional side:", round(missing, 2))
        else:
            print("Side lengths must be positive.")

    elif choice == "3":
        ab = float(input("Enter first segment length: "))
        bc = float(input("Enter second segment length: "))
        ad = float(input("Enter third segment length: "))
        de = float(input("Enter fourth segment length: "))

        if ab > 0 and bc > 0 and ad > 0 and de > 0:
            if abs((ab / bc) - (ad / de)) < 0.000001:
                print("The segments are proportional.")
                print("The Basic Proportionality Theorem is satisfied.")
            else:
                print("The segments are not proportional.")
                print("The theorem is not satisfied.")
        else:
            print("Segment lengths must be positive.")

    else:
        print("Invalid choice.")

triangleproportionality()