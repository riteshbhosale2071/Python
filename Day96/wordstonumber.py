def wordstonumber():
    words = {
        "zero": "0", "one": "1", "two": "2", "three": "3",
        "four": "4", "five": "5", "six": "6", "seven": "7",
        "eight": "8", "nine": "9"
    }

    print("Enter digits in words (Example: one two three four)")
    text = input("Enter words: ").lower()

    result = ""

    for word in text.split():
        if word in words:
            result += words[word]

    print("Number:", result)

wordstonumber()