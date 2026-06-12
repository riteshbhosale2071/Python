def alarm():
    hour = int(input("Enter current hour (0-23): "))
    
    after = int(input("Alarm after how many hours? "))

    alarm_time = (hour + after) % 24

    print("Alarm Will Ring At:", alarm_time, ":00")

alarm()