def typing():
    words = int(input("Enter number of words typed: "))
    
    minutes = float(input("Enter time taken (minutes): "))

    wpm = words / minutes

    print("Typing Speed =", wpm, "WPM")

typing()