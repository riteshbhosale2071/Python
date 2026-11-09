def quadraticequation():
    try:
        a = int(input("Enter minimum value for coefficient a: "))
        b = int(input("Enter minimum value for coefficient b: "))
        c = int(input("Enter minimum value for coefficient c: "))

        a_max = int(input("Enter maximum value for coefficient a: "))
        b_max = int(input("Enter maximum value for coefficient b: "))
        c_max = int(input("Enter maximum value for coefficient c: "))

        if a > a_max or b > b_max or c > c_max:
            print("Invalid coefficient ranges.")
            return

        print("\nGenerated Quadratic Equations:")
        count = 0

        for i in range(a, a_max + 1):
            if i == 0:
                continue

            for j in range(b, b_max + 1):
                for k in range(c, c_max + 1):
                    equation = f"{i}x²"

                    if j > 0:
                        equation += f" + {j}x"
                    elif j < 0:
                        equation += f" - {abs(j)}x"

                    if k > 0:
                        equation += f" + {k}"
                    elif k < 0:
                        equation += f" - {abs(k)}"

                    print(equation + " = 0")
                    count += 1

        print("\nTotal Equations Generated:", count)

    except ValueError:
        print("Please enter valid integer values.")

quadraticequation()