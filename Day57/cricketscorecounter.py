def counter():
    score = 0

    overs = int(input("Enter number of balls: "))

    for i in range(overs):

        runs = int(input(f"Runs on ball {i+1}: "))

        score += runs

    print("Total Score =", score)

counter()