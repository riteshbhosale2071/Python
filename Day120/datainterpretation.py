def datainterpretation():
    print("Data Interpretation Quiz")
    print("Sales Data: January = 120, February = 150")
    
    answer = input("Which month had higher sales? ").strip().lower()

    if answer == "february":
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: February")

datainterpretation()