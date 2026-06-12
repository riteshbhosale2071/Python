import time

def stopwatch():
    seconds = int(input("Enter number of seconds: "))

    for i in range(seconds + 1):
        print(i)
        time.sleep(1)

    print("Stopwatch Finished")

stopwatch()