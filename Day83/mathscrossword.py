def crossword():
    words = {
        "ADD": "Addition",
        "SUB": "Subtraction",
        "MUL": "Multiplication",
        "DIV": "Division",
        "SUM": "Total",
        "ODD": "Not divisible by 2",
        "EVEN": "Divisible by 2"
    }

    clue = input("Enter clue (Addition, Subtraction, Multiplication, Division, Total, Not divisible by 2, Divisible by 2): ")

    found = False

    for word, meaning in words.items():
        if clue.lower() == meaning.lower():
            print("Answer =", word)
            found = True
            break

    if not found:
        print("No matching word found.")

crossword()