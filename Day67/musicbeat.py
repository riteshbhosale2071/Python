def music():
    beats = int(input("Enter number of beats: "))
    
    seconds = float(input("Enter time in seconds: "))

    bpm = (beats / seconds) * 60

    print("BPM =", bpm)

music()