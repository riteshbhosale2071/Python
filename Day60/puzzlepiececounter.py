def puzzle():
    total_pieces = int(input("Enter total puzzle pieces: "))

    joined_pieces = int(input("Enter pieces joined: "))

    remaining = total_pieces - joined_pieces

    print("Joined Pieces =", joined_pieces)

    print("Remaining Pieces =", remaining)

puzzle()