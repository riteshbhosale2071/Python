def total_seconds(hours, minutes, seconds):
    total = (hours * 3600) + (minutes * 60) + seconds
    return total

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

result = total_seconds(hours, minutes, seconds)

print("Total Seconds =", result)