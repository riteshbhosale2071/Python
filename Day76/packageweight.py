def package():
    weight = float(input("Enter the package weight (kg) :"))

    if weight < 10:
        print("Low Weight")

    elif weight < 50:
        print("Medium Weight")

    else:
        print("Heavy Weight")

package()