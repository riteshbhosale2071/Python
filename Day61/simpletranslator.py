def translate():
    words = {
        "hello": "namaste",
        "thank you": "dhanyavad",
        "goodbye": "alvida",
        "yes": "haan",
        "no": "nahi"
    }

    word = input("Enter English word: ").lower()

    print("Translation =", words.get(word, "Word not found"))

translate()