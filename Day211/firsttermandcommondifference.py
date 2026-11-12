def firsttermandcommondifference():
    try:
        n = int(input("Enter term number (n): "))
        nth_term = float(input("Enter nth term: "))
        m = int(input("Enter another term number (m): "))
        mth_term = float(input("Enter mth term: "))

        if n <= 0 or m <= 0:
            print("Term positions must be greater than zero.")
            return

        if n == m:
            print("Term positions must be different.")
            return

        common_difference = (mth_term - nth_term) / (m - n)
        first_term = nth_term - (n - 1) * common_difference

        print("\nArithmetic Progression Details:")
        print("First Term:", round(first_term, 4))
        print("Common Difference:", round(common_difference, 4))

        print("\nVerification:")
        print(f"Term {n}:", round(first_term + (n - 1) * common_difference, 4))
        print(f"Term {m}:", round(first_term + (m - 1) * common_difference, 4))

    except ValueError:
        print("Please enter valid numeric values.")

firsttermandcommondifference()