def complementaryevent():
    print("Complementary Event Calculator")

    total_outcomes = int(input("Enter total number of possible outcomes: "))
    favorable_outcomes = int(input("Enter favorable outcomes for event A: "))

    if total_outcomes <= 0:
        print("Total outcomes must be greater than zero.")
        return

    if favorable_outcomes < 0 or favorable_outcomes > total_outcomes:
        print("Invalid number of favorable outcomes.")
        return

    complement_outcomes = total_outcomes - favorable_outcomes

    probability_a = favorable_outcomes / total_outcomes
    probability_not_a = complement_outcomes / total_outcomes

    print("\nComplementary Event Results :")
    print("Total Outcomes:", total_outcomes)
    print("Favorable Outcomes of A:", favorable_outcomes)
    print("Favorable Outcomes of A':", complement_outcomes)

    print(f"\nProbability of A: {probability_a:.4f}")
    print(f"Probability of Complement A': {probability_not_a:.4f}")

    print(f"\nP(A) + P(A'): {probability_a + probability_not_a:.4f}")

complementaryevent()