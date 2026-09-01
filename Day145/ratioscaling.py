def ratioscaling():
    print("Enter the original ratio A : B")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))

    if a <= 0 or b <= 0:
        print("Ratio values must be positive.")
        return

    scale = float(input("Enter scaling factor: "))

    if scale <= 0:
        print("Scaling factor must be positive.")
        return

    new_a = a * scale
    new_b = b * scale

    print("\nRatio Scaling :")
    print("Original Ratio:", a, ":", b)
    print("Scaling Factor:", scale)
    print("Scaled Ratio:", new_a, ":", new_b)

ratioscaling()