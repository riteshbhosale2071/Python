def probabilityofanevent():
    print("Probability of an Event Calculator")

    total_outcomes = int(input("Enter total number of possible outcomes: "))
    favorable_outcomes = int(input("Enter number of favorable outcomes: "))

    if total_outcomes <= 0:
        print("Total outcomes must be greater than zero.")
        return

    if favorable_outcomes < 0 or favorable_outcomes > total_outcomes:
        print("Invalid number of favorable outcomes.")
        return

    probability = favorable_outcomes / total_outcomes
    percentage = probability * 100

    print("\nProbability Result :")
    print("Total Outcomes:", total_outcomes)
    print("Favorable Outcomes:", favorable_outcomes)
    print(f"Probability of Event: {probability:.4f}")
    print(f"Probability Percentage: {percentage:.2f}%")

    if favorable_outcomes == 0:
        print("The event is an impossible event.")
    elif favorable_outcomes == total_outcomes:
        print("The event is a sure event.")
    else:
        print("The event is a possible event.")

probabilityofanevent()