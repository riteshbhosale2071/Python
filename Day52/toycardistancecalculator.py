def find():
    speed = int(input("Enter toy car speed (m/s): "))
    
    time = int(input("Enter time travelled (s): "))

    distance = speed * time

    print("Distance Travelled =", distance, "meters")

find()