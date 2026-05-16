def find():
    t = ("madam", "python", "level", "racecar", "hello")

    longest = ""

    for word in t:
        if word == word[::-1]:

            if len(word) > len(longest):
                longest = word

    print("Longest Palindrome:", longest)
find()