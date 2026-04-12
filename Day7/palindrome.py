num=input("Enter a num: ")
if num==num[::-1]:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")