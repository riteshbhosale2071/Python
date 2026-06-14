import time

def rocket():
    count = int(input("Enter countdown number: "))

    for i in range(count, -1, -1):
        print(i)
        time.sleep(1)

    print("Rocket Launched!")

rocket()