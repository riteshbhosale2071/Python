def constructionstep():
    total_steps = int(input("Enter the total number of construction steps: "))
    completed_steps = int(input("Enter the number of completed steps: "))

    if completed_steps == total_steps:
        print("Construction Completed Successfully.")
    elif completed_steps < total_steps:
        print("Construction Incomplete.")
        print("Remaining Steps:", total_steps - completed_steps)
    else:
        print("Invalid Input! Completed steps cannot exceed total steps.")

constructionstep()