def reverse():
    num = []
    num = input("Enter the number: ")
    rev = num[::-1]
    print(f"Reverse of {num} is",rev)

    if rev == num:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")

reverse()