import matplotlib.pyplot as plt
import numpy as np

def graphicalequation():
    print("Graphical Equation Analyzer")
    print("\nEquation Format: y = mx + c")

    m = float(input("Enter slope (m): "))
    c = float(input("Enter y-intercept (c): "))

    x = np.linspace(-10, 10, 100)
    y = m * x + c

    print("\nEquation Analysis:")
    print(f"Equation: y = {m}x + {c}")
    print("Slope:", m)
    print("Y-Intercept:", c)

    if m > 0:
        print("The line is increasing.")
    elif m < 0:
        print("The line is decreasing.")
    else:
        print("The line is horizontal.")

    if m != 0:
        x_intercept = -c / m
        print("X-Intercept:", round(x_intercept, 2))
    else:
        print("X-Intercept: No unique x-intercept." if c != 0 else "Every point on the x-axis is an intercept.")

    plt.plot(x, y, label=f"y = {m}x + {c}")
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title("Graphical Equation Analyzer")
    plt.grid(True)
    plt.legend()
    plt.show()

graphicalequation()