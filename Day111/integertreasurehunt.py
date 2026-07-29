def integertreasurehunt():
    treasure = 25

    guess = int(input("Guess the hidden integer: "))

    if guess == treasure:
        print("Congratulations! You found the treasure.")
    else:
        print("Wrong guess! The hidden integer was", treasure)

integertreasurehunt()