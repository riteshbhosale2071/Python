def symmetricpattern():
    text = input("Enter a pattern: ")

    if text == text[::-1]:
        print("Pattern is Symmetric")
    else:
        print("Pattern is Not Symmetric")

symmetricpattern()