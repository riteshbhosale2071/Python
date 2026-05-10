def find():
    temp = int(input("Enter the value of temperature(C): "))
    humd = int(input("Enter the value of humidity(%): "))
    if temp >= 30 and humd >= 90:
        print("It's Hot and Humid")
    elif temp >= 30 and humd <90 :
        print("It's Hot")
    elif temp < 30 and humd >= 90:
        print("It's Cool and Humid")
    elif temp < 30 and humd < 90 :
        print("It's Cool")
    else:
        print("Enter valid values")

find()