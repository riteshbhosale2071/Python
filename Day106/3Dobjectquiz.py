def objectquiz():
    answer = input("Which 3D shape has no edges? ").lower()

    if answer == "sphere":
        print("Correct!")
    else:
        print("Wrong!")
        print("Correct Answer: Sphere")

objectquiz()