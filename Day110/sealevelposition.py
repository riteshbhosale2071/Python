def sealevelposition():
    position = int(input("Enter the position relative to sea level: "))

    if position > 0:
        print("Above Sea Level")
    elif position < 0:
        print("Below Sea Level")
    else:
        print("At Sea Level")

sealevelposition()