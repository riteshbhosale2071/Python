def count_case(s):

    upper = 0
    lower = 0

    for i in s:

        if i.isupper():
            upper += 1

        elif i.islower():
            lower += 1

    return {"Uppercase": upper, "Lowercase": lower}


string = input("Enter string: ")

print(count_case(string))