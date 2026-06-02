import time
def timer():
    minutes = int(input("Enter lunch break time (minutes): "))

    seconds = minutes * 60

    while seconds > 0:

        mins = seconds // 60
        secs = seconds % 60

        print(f"{mins:02d}:{secs:02d}")

        time.sleep(1)

        seconds -= 1

    print("Lunch Break Over!")

timer()